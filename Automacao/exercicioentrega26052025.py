import os
import shutil
import datetime

def criar_backup(caminho_banco_dados, pasta_backup):
    # Verifica se o arquivo do banco de dados existe
    if not os.path.exists(caminho_banco_dados):
        print("Arquivo do banco de dados não encontrado.")
        return
    
    # Cria a pasta de backup se ela não existir
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)
        print(f"Pasta de backup criada em: {pasta_backup}")
    
    # Gera um nome de arquivo com timestamp para o backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_backup = f"backup_{timestamp}.sql"
    caminho_backup = os.path.join(pasta_backup, nome_backup)
    
    try:
        # Copia o arquivo do banco de dados para a pasta de backup
        shutil.copy2(caminho_banco_dados, caminho_backup)
        print(f"Backup realizado com sucesso: {caminho_backup}")
    except Exception as e:
        print(f"Erro ao fazer backup: {e}")

# Exemplo de uso
caminho_banco = "meu_banco_de_dados.sql"  # Caminho do seu banco de dados
pasta_de_backup = " backups"  # Pasta onde os backups serão armazenados

criar_backup(caminho_banco, pasta_de_backup)