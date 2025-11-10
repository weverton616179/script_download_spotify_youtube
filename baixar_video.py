import yt_dlp
from spotdl import Spotdl
from spotdl.types.options import DownloaderOptions

def download_video_youtube(url, qualidade, formato):
    ydl_opts = {
        'format': (
            f'bestvideo[ext=webm][height<={qualidade}]+bestaudio[ext=webm]/best[ext=webm]'if formato == "webm"
            else f'bestvideo[height<={qualidade}]+bestaudio/best'
        ),
        'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',
        'merge_output_format': formato, # formato final do video
        'postprocessor_args': ['-c:v', 'copy', '-c:a', 'copy' if formato == "webm" else 'aac'],
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': formato}],
        'ignoreerrors': True,
        'extract_flat': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"--------------Baixando: {url}--------------")
        ydl.download([url])
        print("--------------Download finalizado com sucesso--------------")

def download_audio_youtube(url, qualidade, formato):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': formato,
                'preferredquality': qualidade,
            }
        ],
        'ignoreerrors': True,
        'extract_flat': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"--------------Baixando: {url}--------------")
        ydl.download([url])
        print("--------------Download finalizado com sucesso--------------")

def download_spotify(url, formato):
    downloader_options = DownloaderOptions(
        output="{artists} - {title}.{output-ext}",
        format=formato,
    )
    spotdl = Spotdl(
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        downloader_settings=downloader_options
    )
    musicas = spotdl.search([url])

    for musica in musicas:
        spotdl.download(musica)

if __name__ == "__main__":
    print("--------------Downloader de videos, musicas e playlists--------------")
    print("Escolha uma opção:")
    print("1 - Baixar videos do YouTube")
    print("2 - Baixar audios do YouTube")
    print("3 - Baixar musicas do Spotify")
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == '1':
        url = input("Coloque o link do video ou playlist:")
        
        print("--------------Escolha a qualidade do video--------------")
        print("-----Caso a qualidade não esteja disponivel, o video sera baixado na maior qualidade possivel-----")
        print("1 - 2160p")
        print("2 - 1440p")
        print("3 - 1080p")
        print("4 - 720p")
        print("5 - 480p")
        print("6 - 360p")
        print("7 - 240p")
        print("8 - 144p")
        qualidade_escolhida = input("Digite o número da qualidade desejada: ")
        qualidade_opcoes = {
            '1': '2160',
            '2': '1440',
            '3': '1080',
            '4': '720',
            '5': '480',
            '6': '360',
            '7': '240',
            '8': '144'
        }
        qualidade = qualidade_opcoes.get(qualidade_escolhida)
        
        print("--------------Escolha o formato do video--------------")
        print("1 - mp4")
        print("2 - mkv")
        print("3 - webm")
        formato_escolhido = input("Digite o número do formato desejado: ")
        formato_opcoes = {
            '1': 'mp4',
            '2': 'mkv',
            '3': 'webm'
        }
        formato = formato_opcoes.get(formato_escolhido)
        
        download_video_youtube(url, qualidade, formato)
        print("Download concluido")
    elif escolha == '2':
        url = input("Coloque o link do video ou playlist:")
        print("--------------Escolha a qualidade do audio--------------")
        print("1 - 320kbps")
        print("2 - 256kbps")
        print("3 - 192kbps")
        print("4 - 160kbps")
        print("5 - 128kbps")
        print("6 - 96kbps")
        qualidade_escolhida = input("Digite o número da qualidade desejada: ")
        qualidade_opcoes = {
            '1': '320',
            '2': '256',
            '3': '192',
            '4': '160',
            '5': '128',
            '6': '96'
        }
        qualidade = qualidade_opcoes.get(qualidade_escolhida)
        
        print("--------------Escolha o formato do audio--------------")
        print("1 - mp3")
        print("2 - m4a")
        print("3 - wav")
        print("4 - flac")
        print("5 - aac")
        print("6 - opus")
        formato_escolhido = input("Digite o número do formato desejado: ")
        formato_opcoes = {
            '1': 'mp3',
            '2': 'm4a',
            '3': 'wav',
            '4': 'flac',
            '5': 'aac',
            '6': 'opus'
        }
        formato = formato_opcoes.get(formato_escolhido)
        
        download_audio_youtube(url, qualidade, formato)
        print("Download concluido")
    elif escolha == '3':
        url = input("Coloque o link da musica ou playlist:")
        
        print("--------------Escolha o formato do audio--------------")
        print("1 - mp3")
        print("2 - m4a")
        print("3 - wav")
        print("4 - flac")
        print("5 - aac")
        print("6 - opus")
        formato_escolhido = input("Digite o número do formato desejado: ")
        formato_opcoes = {
            '1': 'mp3',
            '2': 'm4a',
            '3': 'wav',
            '4': 'flac',
            '5': 'aac',
            '6': 'opus'
        }
        formato = formato_opcoes.get(formato_escolhido)
        
        download_spotify(url, formato)
        print("Download concluido")
    else:
        print("Opção inválida.")
