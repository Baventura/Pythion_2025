import openpyxl
from urllib.parse import quote  # decodifica a mensagem enviada via URL
import webbrowser
from time import sleep
import pyautogui
from datetime import date, datetime

# Abre o WhatsApp Web no navegador
webbrowser.open('https://web.whatsapp.com/')
print("Por favor, escaneie o QR code e aguarde a carga do WhatsApp Web.")
sleep(20)  # Tempo para o WhatsApp Web carregar

# Carrega a planilha de devedores
workbook = openpyxl.load_workbook('devedores.xlsx')
pagina_cliente = workbook['Plan1']

for linha in pagina_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    status = linha[2].value
    data_de_pagamento = linha[3].value

    # Verifica se os dados essenciais estão presentes
    if nome is None or telefone is None:
        continue  # Pula para a próxima linha se faltar algum dado

    # Formata a data de pagamento, se for uma data válida
    if isinstance(data_de_pagamento, (date, datetime)):
        data_formatada = data_de_pagamento.strftime("%d/%m/%Y")
    elif data_de_pagamento is not None:
        data_formatada = str(data_de_pagamento)
    else:
        data_formatada = "não informada"

    # Cria a mensagem personalizada
    mensagem = f'Olá {nome}, seu débito está em atraso ({status}) desde {data_formatada}. Por favor, realize o pagamento.'

    # Cria o link do WhatsApp com a mensagem codificada
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

    # Abre o link no navegador
    webbrowser.open(link_mensagem_whatsapp)
    print(f'Abrindo conversa com {nome}...')
    sleep(10)  # Aguarda o WhatsApp abrir a conversa

    # Envia a mensagem pressionando Enter
    pyautogui.press('enter')
    print(f'Mensagem enviada para {nome}.')

    sleep(5)  # Pequena pausa antes de fechar a aba
    # Fecha a aba do navegador (Ctrl + W)
    pyautogui.hotkey('ctrl', 'w')
    sleep(2)  # Aguarda fechar a aba antes de continuar