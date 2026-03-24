import socket
import pyperclip
import threading

# Configurações de Rede
# '0.0.0.0' faz o servidor ouvir em todas as placas de rede, incluindo o Hamachi
IP_ESCUTA = '0.0.0.0'
PORTA = 9870

# Lista para armazenar o histórico (máximo 5 itens)
historico = []

# Função que permite ao usuário do servidor escolher um item para "Colar"
def menu_selecao():
    while True:
        input("\n Pressione ENTER para abrir o menu de seleção de Ctrl+V \n")
        
        if not historico:
            print("Histórico ainda está vazio.")
            continue

        print("\n ÚLTIMOS 5 TEXTOS RECEBIDOS")
        for i, texto in enumerate(historico):
            # Mostra o índice e os primeiros 30 caracteres do texto
            print(f"[{i}] {texto[:30]}...")

        try:
            opcao = int(input("\nQual número você deseja colar agora? "))
            if 0 <= opcao < len(historico):
                # Define o texto escolhido como o novo Ctrl+C local do servidor
                pyperclip.copy(historico[opcao])
                print(f"Pronto! Texto '{historico[opcao][:20]}' está pronto para Ctrl+V.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número.")

# Configuração do Socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_ESCUTA, PORTA))

# Inicia a thread do menu para que ela rode ao mesmo tempo que o recebimento
thread_menu = threading.Thread(target=menu_selecao, daemon=True)
thread_menu.start()

print(f"Servidor aguardando mensagens na porta {PORTA}...")

try:
    while True:
        # Recebe os dados (até 4096 bytes)
        dados, endereco = server_socket.recvfrom(4096)
        texto_recebido = dados.decode('utf-8')

        print(f"\n[LOG] Mensagem recebida de {endereco}")

        # Lógica de acumular as últimas 5 cópias
        if len(historico) >= 5:
            historico.pop(0) # Remove a mais antiga (índice 0)
        
        historico.append(texto_recebido)

except KeyboardInterrupt:
    print("\nDesligando servidor...")
finally:
    server_socket.close()