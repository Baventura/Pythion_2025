import os
import shutil
from datetime import datetime
import glob

# Configurações
arquivo_origem = 'seu_banco_de_dados.csv'  # Troque pelo seu arquivo
pasta_backup = 'backups'

# 1. Verifica se a pasta backups existe, se não, cria
if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)

# 2. Copia o arquivo original para a pasta backups com a data e hora no nome
agora = datetime.now().strftime('%Y%m%d_%H%M%S')
nome_backup = f"{os.path.splitext(os.path.basename(arquivo_origem))[0]}backup{agora}{os.path.splitext(arquivo_origem)[1]}"
caminho_backup = os.path.join(pasta_backup, nome_backup)

try:
    shutil.copy2(arquivo_origem, caminho_backup)
    print(f"Backup criado com sucesso: {nome_backup}")
except Exception as e:
    print(f"Erro ao criar backup: {e}")

# 3. Mantém apenas os 5 backups mais recentes
backups = sorted(glob.glob(os.path.join(pasta_backup, 'backup' + os.path.splitext(arquivo_origem)[1])), key=os.path.getmtime, reverse=True)

# Exclui backups mais antigos, mantendo apenas os 5 mais recentes
for backup_antigo in backups[5:]:
    try:
        os.remove(backup_antigo)
        print(f"Backup antigo removido: {os.path.basename(backup_antigo)}")
    except Exception as e:
        print(f"Erro ao remover backup antigo: {e}")

print("Operação de backup concluída com sucesso!")