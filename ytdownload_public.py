from pytube import YouTube
import os
import urllib.request
import re
from time import sleep as sl

#pyinstaller --onefile <caminho para o arquivo python>  ***para transformar um .py em executavel
#filtros = input("Quais filtros quer aplicar:")
#yt.filter(filtros)
#yt.streams.filter(file_extension='mp4')
#yt.streams.order_by("resolution")
#yt.streams.filter(type="audio").last()
  
def play_music(music_path,music2):
    music_path = music_path.replace('"','')
    music_path = music_path[:3]+'"'+music_path[3:]+'"'
    os.system('cls')
    print("-*"*20)
    print(f'Nome do arquivo que estou tocando:{music2}')
    print("-*"*20)
    os.system(f'start {music_path}')
    sl(2)
    
def search(pesq):
    pesq = pesq.replace(' ','+')
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={pesq}")
    videoId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = f"https://www.youtube.com/watch?v={videoId[0]}"
    return url

def HUD_download():
    os.system('cls')
    print("Categorias existentes...\nSe quiser, coloque um nome novo para criar uma nova categoria")
    print("-*"*20)
    if os.path.exists("C:\\musicas") == False:
        os.system("mkdir C:\\musicas")
    os.system("dir /B /AD C:\\musicas")
    print("-*"*20)
    tag = input("ENTRADA:")
    os.system('cls')
    print("-*"*20)
    link = input("URL do video:")
    os.system('cls')
    print("-*"*20)
    play = input("Deseja iniciar a musica depois do download? \n1 - sim\n2 - nao\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nENTRADA:")
    download(link,play,tag)
    
def HUD_download2(link):
    os.system('cls')
    print("Categorias existentes...\nSe quiser, coloque um nome novo para criar uma nova categoria")
    print("-*"*20)
    if os.path.exists("C:\\musicas") == False:
        os.system("mkdir C:\\musicas")
    os.system("dir /B /AD C:\\musicas")
    print("-*"*20)
    tag = input("ENTRADA:")
    os.system('cls')
    print("-*"*20)
    play = input("Deseja iniciar a musica depois do download? \n1 - sim\n2 - nao\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nENTRADA:")
    download(link,play,tag)
    
def HUD_pesquisa():
    os.system('cls')
    print("-*"*20)
    print("Digite a sua pesquisa")
    print("-*"*20)
    pesq=input("ENTRADA:")
    link=search(pesq)
    HUD_download2(link)

def HUD_main():
    os.system('cls')
    print("codigo escrito por undertown_ aproveite")
    sl(1.5)
    os.system('cls')
    print("-*"*20)
    resp=input("1 - Baixar com link \n2 - Pesquisar\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nENTRADA:")
    if resp == '1' or resp.lower() == 'baixar com link':
        HUD_download()
    elif resp == '2' or resp.lower() == 'pesquisar':
        HUD_pesquisa()

def download(link,play,tag):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True,mime_type="audio/mp4").last()
    if "&" in audio.title:
        audio_title = audio.title.replace("&","")
    elif "'" in audio.title:
        audio_title = audio.title.replace("'","")
    elif "'" in audio.title:
        audio_title = audio.title.replace('"',"")
    else:
        audio_title = audio.title
    if tag != '':
        etags = os.popen('dir /B /AD C:\\musicas').read()
        etags = etags.split("\n")
        etags = etags[:-1]
        if tag not in etags:
            os.system(f'mkdir "C:\\musicas\\{tag}"')
        audio.download(f'C:\\musicas\\{tag}',f'{audio_title}.mp3')
        music = f"{audio_title}.mp3"
        music2 = music.replace(" ","")
        os.rename(f'C:\\musicas\\{tag}\\{music}',f'C:\\musicas\\{tag}\\{music2}')
        music_path = (f'"C:\\musicas\\{tag}\\{music2}"')
    else:
        audio.download("C:\\musicas\\",f"{audio_title}.mp3")
        music = f"{audio_title}.mp3"
        music2 = music.replace(" ","")
        os.rename(f'C:\\musicas\\{music}',f'C:\\musicas\\{music2}')
        music_path = (f'C:\\musicas\\{tag}\\{music2}')

    if play == "1" or play.lower() == "sim":
        play_music(music_path,music2)
        
while True:
    HUD_main()
    os.system('cls')
    print("-*"*20)
    res = input("Aperte enter para baixar outra musica ou ctrl+c para finalizar o programa \n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")