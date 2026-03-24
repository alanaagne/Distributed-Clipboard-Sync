import socket
import time
import pyperclip  # Biblioteca para ler/escrever no Ctrl+C

# Configurações de Rede
# Substitua pelo IP do Hamachi da máquina do Servidor
IP_SERVIDOR = '25.xx.xx.xx' 
PORTA = 9870

# Criação do Socket UDP
# AF_INET = IPV4 | SOCK_DGRAM = UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Monitorando sua área de transferência (Ctrl+C)...")

ultimo_texto = ""

try:
    while True:
        # Pega o texto atual do Ctrl+C do Windows/Mac/Linux
        texto_atual = pyperclip.paste()

        # Só envia se o texto mudou e não estiver vazio
        if texto_atual != ultimo_texto and texto_atual.strip() != "":
            print(f"Novo texto detectado: {texto_atual[:20]}...")
            
            # Envia o texto convertido em bytes para o servidor
            client_socket.sendto(texto_atual.encode('utf-8'), (IP_SERVIDOR, PORTA))
            
            ultimo_texto = texto_atual
            print("Enviado com sucesso!")

        # Espera 1 segundo antes de checar de novo para não sobrecarregar o PC
        time.sleep(1)

except KeyboardInterrupt:
    print("\nEncerrando cliente...")
finally:
    client_socket.close()