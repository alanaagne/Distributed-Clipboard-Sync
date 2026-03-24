# 📋 ClipSync-UDP: Histórico de Área de Transferência Distribuído

Este projeto foi desenvolvido como parte do **Seminário de Sistemas Distribuídos**, com foco em **Comunicação entre Processos (IPC)** utilizando Sockets UDP.

## 🚀 Sobre o Projeto

O objetivo deste sistema é permitir o compartilhamento e a sincronização da área de transferência (Ctrl+C) entre diferentes máquinas em uma rede. O sistema monitora o clipboard do cliente e mantém um histórico das últimas 5 entradas no servidor, permitindo que o usuário do servidor escolha qual texto deseja "colar" localmente.

### Temas Abordados:
* **Comunicação entre Processos:** Troca de mensagens via Sockets.
* **Arquitetura Cliente-Servidor:** Implementação clássica de requisição e resposta.
* **Sincronização de Dados:** Gerenciamento de estado entre nós remotos.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Protocolo de Rede:** UDP (User Datagram Protocol)
* **Bibliotecas:** 
  * `socket`: Comunicação de rede de baixo nível.
  * `pyperclip`: Manipulação da área de transferência do sistema operacional.
  * `threading`: Processamento paralelo para o menu interativo do servidor.
* **Rede Virtual:** LogMeIn Hamachi (para simular comunicação WAN).

## 📦 Como Instalar e Rodar
### Pré-requisitos
Certifique-se de ter o Python instalado e baixe o requirements.txt ou baixe diretamente a biblioteca:
```bash
pip install pyperclip
```
### Configuração da Rede
- Ambos os computadores devem estar na mesma rede ou conectados via VPN.
- Obtenha o IP do servidor na rede virtual.

### Execução

- No Servidor:
```
python servidor.py
```

- No Cliente (Altere a variável IP_SERVIDOR no código para o IP correto):
```
python cliente.py
```

## 📖 Regras de Negócio
- O cliente envia automaticamente qualquer novo texto copiado.

- O servidor armazena as últimas cinco cópias de texto recebidas.

- O servidor oferece um menu para selecionar qual das 5 cópias será enviada para o clipboard local (Ctrl+V).