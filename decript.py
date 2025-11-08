import os
from cryptography.fernet import Fernet


try:
    with open("chave.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    print("ERRO: Arquivo 'chave.key' não encontrado.")
    print("Você precisa da chave para descriptografar os arquivos.")
    exit()


f = Fernet(key)


pasta_alvo = "documentos_vitima"
extensoes_alvo = ['.txt'] 

print(f"Iniciando descriptografia na pasta '{pasta_alvo}'...")

for filename in os.listdir(pasta_alvo):
    
    if any(filename.endswith(ext) for ext in extensoes_alvo):
        filepath = os.path.join(pasta_alvo, filename)
        
        try:
            
            with open(filepath, "rb") as file:
                encrypted_data = file.read()
                
            
            decrypted_data = f.decrypt(encrypted_data)
            
            
            with open(filepath, "wb") as file:
                file.write(decrypted_data)
                
            print(f"  [DESCRIPTOGRAFADO] -> {filename}")
            
        except Exception as e:
            print(f"  [FALHA] -> Não foi possível descriptografar {filename}: {e}")


try:
    os.remove(os.path.join(pasta_alvo, "LEIA_ME_PARA_RESGATE.txt"))
    print("\nNota de resgate removida.")
except FileNotFoundError:
    pass

print("Processo de descriptografia concluído.")