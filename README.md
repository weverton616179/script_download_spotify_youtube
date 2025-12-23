🎬 Downloader de Vídeos e Músicas (YouTube & Spotify)

Um script em Python para baixar vídeos, áudios e playlists do YouTube e músicas/playlists do Spotify, com escolha de qualidade e formato via terminal.

O projeto usa:

yt-dlp
 para downloads do YouTube

spotDL
 para downloads do Spotify

ffmpeg para conversão e junção de áudio/vídeo

✨ Funcionalidades
✅ YouTube

Baixar vídeos ou playlists

Escolher resolução (2160p até 144p)

Escolher formato de vídeo (mp4, mkv, webm)

Baixar apenas áudio

Escolher qualidade do áudio (96kbps até 320kbps)

Escolher formato de áudio (mp3, m4a, wav, flac, etc.)

✅ Spotify

Baixar músicas ou playlists

Escolher formato de áudio

Nome automático: Artista - Música.ext

📁 Estrutura do Projeto
📦 projeto
 └── baixar_video.py

🧰 Requisitos

Antes de rodar o projeto, você precisa ter instalado:

🔹 Python

Python 3.9 ou superior

Verifique:

python --version

🔹 FFmpeg

O ffmpeg é obrigatório para juntar e converter áudio/vídeo.

Windows

Baixe ffmpeg-git-essentials.7z em: https://www.gyan.dev/ffmpeg/builds/

Adicione o ffmpeg ao PATH do sistema

Teste:

ffmpeg -version

Linux (Debian/Ubuntu)
sudo apt install ffmpeg

📦 Instalação das Dependências

Instale as bibliotecas Python necessárias:

pip install yt-dlp spotdl

🔐 Configuração do Spotify (IMPORTANTE)

Para baixar músicas do Spotify, você precisa de credenciais da API do Spotify.

1️⃣ Crie um app no Spotify Developer

Acesse:

https://developer.spotify.com/


Crie um app e copie:

CLIENT_ID

CLIENT_SECRET

2️⃣ Configure no código

No arquivo baixar_video.py, altere:

spotdl = Spotdl(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    downloader_settings=downloader_options
)


Substitua pelos seus dados reais.

▶️ Como Usar

Execute o script no terminal:

python baixar_video.py


Você verá o menu:

--------------Downloader de videos, musicas e playlists--------------
Escolha uma opção:
1 - Baixar videos do YouTube
2 - Baixar audios do YouTube
3 - Baixar musicas do Spotify

🎥 Opção 1 — Baixar Vídeos do YouTube

Cole o link do vídeo ou playlist

Escolha a qualidade (ex: 1080p)

Escolha o formato (mp4, mkv ou webm)

O download começa automaticamente

📌 Se a qualidade não existir, o script baixa a melhor disponível.

🎧 Opção 2 — Baixar Áudio do YouTube

Cole o link do vídeo ou playlist

Escolha a qualidade do áudio

Escolha o formato (mp3, flac, opus, etc.)

O áudio será extraído e convertido

🎵 Opção 3 — Baixar Músicas do Spotify

Cole o link da música ou playlist

Escolha o formato do áudio

As músicas serão buscadas no YouTube e baixadas automaticamente

📂 Organização dos Arquivos

YouTube:

01 - Nome do Vídeo.mp4
02 - Outro Vídeo.mkv


Spotify:

Artista - Música.mp3

⚠️ Observações Importantes

O script não burla DRM

Downloads dependem da disponibilidade pública do conteúdo

Use apenas para uso pessoal e educacional

Playlists grandes podem demorar

🚀 Possíveis Melhorias Futuras

Interface gráfica (GUI)

Download paralelo

Escolha de pasta de saída

Detecção automática de ffmpeg

Arquivo .env para credenciais Spotify

📜 Licença

Este projeto é de uso livre para fins educacionais e pessoais.
O uso indevido do conteúdo baixado é de responsabilidade do usuário.
