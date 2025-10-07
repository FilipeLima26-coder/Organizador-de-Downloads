#importa bibliotecas necessárias
import os
import shutil

#caminho da pasta que vai ser organizada
pasta_downloads = r"E:\Lipe Teste"

#dicionário com as categorias e extensões de arquivos
categorias = {"Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Músicas": [".mp3", ".wav", ".ogg", ".flac"],
    "Programas": [".exe", ".msi"],}

#Função para descobrir a categoria pela extensãodo arquivo

def descobrir_categoria(extensao):
    for categoria, extensoes in categorias.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"


#loop pelos arquivos da pasta
for nome_arquivo in os.listdir(pasta_downloads):
    caminho_arquivo = os.path.join(pasta_downloads, nome_arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    #pega a extensão do arquivo
    _, extensao = os.path.splitext(nome_arquivo)

    #descobre a categoria do arquivo
    categoria = descobrir_categoria(extensao)

    #cria o caminho da pasta de destino

    pasta_destino = os.path.join(pasta_downloads, categoria)

    #cria a pasta de destino se não existir
    os.makedirs(pasta_destino, exist_ok=True)

    #move o arquivo

    shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
    print(f'Movido: {nome_arquivo} para {categoria}')

print("Organização concluída!")