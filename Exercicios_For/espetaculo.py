import os
from tkinter.filedialog import askdirectory
import shutil
import datetime
import time

while True:
    # Seleciona a pasta que será feita o backup
    pasta_selecionada = askdirectory()
    print(f"Pasta selecionada: {pasta_selecionada}")

    # Define o nome da pasta de backup dentro da pasta selecionada
    nome_pasta_backup = 'backup'
    # Cria o caminho completo para a pasta de backup
    nome_completo_backup = os.path.join(pasta_selecionada, nome_pasta_backup)

    # Cria a pasta 'backup' se ela ainda não existir
    if not os.path.exists(nome_completo_backup):
        os.mkdir(nome_completo_backup)

    # Gera um nome único para o backup com base na data e hora atual
    data_hora = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nome_backup_especifico = f"{data_hora}"
    caminho_backup_especifico = os.path.join(nome_completo_backup, nome_backup_especifico)

    # Cria a pasta específica do backup
    os.mkdir(caminho_backup_especifico)

    # Lista todos os arquivos e pastas na pasta selecionada
    lista_arquivos = os.listdir(pasta_selecionada)

    for arquivo in lista_arquivos:
        # Ignora a pasta de backup para evitar copiar ela mesma
        if arquivo == nome_pasta_backup:
            continue

        caminho_arquivo = os.path.join(pasta_selecionada, arquivo)
        caminho_destino = os.path.join(caminho_backup_especifico, arquivo)

        # Verifica se é arquivo ou pasta e realiza a cópia adequada
        if os.path.isfile(caminho_arquivo):
            shutil.copy2(caminho_arquivo, caminho_destino)
        elif os.path.isdir(caminho_arquivo):
            shutil.copytree(caminho_arquivo, caminho_destino)

    print("Backup realizado com sucesso. Aguardando 5 segundos...")
    # Aguarda 20 segundos antes de repetir o processo
    time.sleep(5)
    