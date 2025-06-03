import openpyxl
from urllib.parse import quote # decodifica a mensagem enviada url
import webbrowser
from time import sleep
import pyautogui
import sys

webbrowser.open('https://web.whatsapp.com/')
sleep(20)

workbook = openpyxl.load_workbook('devedores.xlsx')
pagina_cliente = workbook['Plan1']

for linha in pagina_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    status = linha[2].value
    data_de_pagamento = linha[3].value

    if nome is None or telefone is None:
        break

   
    mensagem = f'Olá {nome} Seu debito está em Atraso {status} por favor realise o pagamento'
    

    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

    webbrowser.open(link_mensagem_whatsapp)


    sleep(10) 
    pyautogui.press('Enter')

    sleep(5)
    pyautogui.hotkey('ctrl', 'w')