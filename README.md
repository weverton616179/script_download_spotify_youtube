<div align="center">

# 🎬 Downloader de Vídeos e Músicas

### YouTube & Spotify · Simples · Rápido · Terminal

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![spotDL](https://img.shields.io/badge/spotDL-latest-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://github.com/spotDL/spotify-downloader)
[![License](https://img.shields.io/badge/Licença-Educacional-blue?style=for-the-badge)](LICENSE)

</div>

---

Um script Python totalmente interativo para baixar **vídeos**, **áudios** e **playlists** do YouTube, além de **músicas** e **playlists** do Spotify — com controle total de qualidade e formato direto do terminal.

> 🎓 Projeto de uso **educacional e pessoal**. Simplicidade e controle na ponta dos dedos.

---

## 📑 Índice

- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração do Spotify](#-configuração-do-spotify)
- [Como Usar](#-como-usar)
- [Opções de Download](#-opções-de-download)
- [Organização dos Arquivos](#-organização-dos-arquivos)
- [Observações](#-observações-importantes)
- [Roadmap](#-roadmap)
- [Licença](#-licença)

---

## ✨ Funcionalidades

### 📹 YouTube — Vídeos

| Recurso | Descrição |
|---|---|
| 🎥 Download de vídeos | Baixa vídeos individuais ou playlists inteiras |
| 📐 Resoluções | **144p** · 240p · 360p · 480p · 720p · 1080p · 1440p · **2160p (4K)** |
| 📦 Formatos | **MP4** · MKV · WebM |
| 🎧 Extração de áudio | Baixa apenas o áudio, sem o vídeo |

### 🎧 YouTube — Áudios

| Recurso | Descrição |
|---|---|
| 🔊 Qualidade | 96kbps · 128kbps · 160kbps · 192kbps · 256kbps · **320kbps** |
| 🎼 Formatos | MP3 · M4A · WAV · FLAC · AAC · Opus |
| 📝 Playlists | Suporte a playlists completas |

### 🎵 Spotify

| Recurso | Descrição |
|---|---|
| 🎵 Músicas | Busca e download de faixas individuais |
| 📋 Playlists | Suporte a playlists inteiras do Spotify |
| 🏷️ Nomeação automática | Arquivos nomeados como `Artista - Música.ext` |
| 🔍 Busca inteligente | As músicas são localizadas automaticamente no YouTube |

---

## 🧠 Tecnologias Utilizadas

<div align="center">

| Tecnologia | Função | Link |
|---|---|---|
| **🐍 Python 3.9+** | Linguagem base do projeto | [python.org](https://www.python.org/) |
| **⬇️ yt-dlp** | Download de vídeos e áudios do YouTube | [github/yt-dlp](https://github.com/yt-dlp/yt-dlp) |
| **🟢 spotDL** | Integração com Spotify (busca via YouTube) | [github/spotDL](https://github.com/spotDL/spotify-downloader) |
| **🎞️ FFmpeg** | Conversão e merge de áudio/vídeo | [ffmpeg.org](https://ffmpeg.org/) |

</div>

---

## 📁 Estrutura do Projeto

```
script_download_spotify_youtube/
├── baixar_video.py   # Script principal com menu interativo
└── README.md         # Documentação do projeto
```

---

## 🧰 Pré-requisitos

### 🐍 Python 3.9+

```bash
python --version
# Deve retornar Python 3.9.x ou superior
```

Caso não tenha, baixe em [python.org](https://www.python.org/downloads/).

### 🎞️ FFmpeg (obrigatório)

O FFmpeg é essencial para **converter formatos** e **combinar faixas de áudio e vídeo**.

<details>
<summary><b>🪟 Windows</b></summary>

1. Acesse [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/)
2. Baixe o arquivo `ffmpeg-git-essentials.7z`
3. Extraia para uma pasta (ex.: `C:\ffmpeg`)
4. Adicione `C:\ffmpeg\bin` ao **PATH** do sistema:
   - Pressione `Win + R` → `sysdm.cpl` → Avançado → Variáveis de Ambiente
   - Edite a variável `Path` e adicione o caminho da pasta `bin`
5. Teste no terminal:

```bash
ffmpeg -version
```
</details>

<details>
<summary><b>🐧 Linux (Debian/Ubuntu)</b></summary>

```bash
sudo apt update && sudo apt install ffmpeg -y
ffmpeg -version
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
brew install ffmpeg
ffmpeg -version
```
</details>

---

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/script_download_spotify_youtube.git
cd script_download_spotify_youtube

# 2. (Recomendado) Crie um ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. Instale as dependências
pip install yt-dlp spotdl
```

---

## 🔐 Configuração do Spotify

> ⚠️ **Necessário apenas para a Opção 3 (download do Spotify).**  
> Se for usar apenas YouTube, pule esta seção.

### 1. Criar um App no Spotify Developer

1. Acesse o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Faça login e clique em **"Create App"**
3. Preencha nome e descrição (qualquer valor serve)
4. Anote as credenciais:
   - `Client ID`
   - `Client Secret`

### 2. Configurar as credenciais no código

Edite o arquivo `baixar_video.py` e localize o trecho:

```python
spotdl = Spotdl(
    client_id="CLIENT_ID",        # ← Substitua pelo seu Client ID
    client_secret="CLIENT_SECRET", # ← Substitua pelo seu Client Secret
    downloader_settings=downloader_options
)
```

> 💡 **Dica:** Nunca compartilhe ou faça commit das suas credenciais reais. Considere usar variáveis de ambiente ou um arquivo `.env` no futuro.

---

## ▶️ Como Usar

No terminal, execute:

```bash
python baixar_video.py
```

O menu interativo será exibido:

```
-------------- Downloader de videos, musicas e playlists --------------
Escolha uma opção:
1 - Baixar videos do YouTube
2 - Baixar audios do YouTube
3 - Baixar musicas do Spotify
```

Basta digitar o número da opção desejada e seguir as instruções.

---

## 🎥 Opções de Download

### Opção 1 — Baixar Vídeos do YouTube

| Passo | Ação |
|---|---|
| 1 | Cole o link do **vídeo** ou **playlist** |
| 2 | Escolha a **resolução** (ex.: `1080p`) |
| 3 | Escolha o **formato** (`mp4`, `mkv` ou `webm`) |

> 📌 Se a resolução escolhida não estiver disponível, o script baixa automaticamente a **melhor qualidade disponível**.

---

### Opção 2 — Baixar Áudio do YouTube

| Passo | Ação |
|---|---|
| 1 | Cole o link do **vídeo** ou **playlist** |
| 2 | Escolha a **qualidade do áudio** (`96kbps` a `320kbps`) |
| 3 | Escolha o **formato** (`mp3`, `m4a`, `wav`, `flac`, `aac`, `opus`) |

> 🎵 O áudio é **extraído e convertido automaticamente** para o formato escolhido.

---

### Opção 3 — Baixar Músicas do Spotify

| Passo | Ação |
|---|---|
| 1 | Cole o link da **música** ou **playlist** do Spotify |
| 2 | Escolha o **formato do áudio** |

> 🔍 As faixas são **buscadas automaticamente no YouTube** para realizar o download.

---

## 📂 Organização dos Arquivos

Após o download, os arquivos são salvos no mesmo diretório do script:

### YouTube

```
01 - Nome do Vídeo.mp4
02 - Outro Vídeo.mkv
03 - Mais um Vídeo.webm
```

### Spotify

```
Artista 1 - Minha Música.mp3
Artista 2 - Outra Faixa.flac
```

---

## ⚠️ Observações Importantes

| ⚠️ | Observação |
|---|---|
| 🔒 | O script **não burla proteções DRM** |
| 🌐 | Downloads dependem da **disponibilidade pública** do conteúdo |
| 🎓 | Uso restrito a fins **pessoais e educacionais** |
| ⏱️ | Playlists grandes podem levar **vários minutos** |
| 🔑 | A API do Spotify exige cadastro prévio no **Spotify Developer** |

---

## 🚀 Roadmap

- [ ] Interface gráfica (GUI) com **Tkinter** ou **PyQt**
- [ ] Suporte a **downloads paralelos** para playlists grandes
- [ ] Seleção de **pasta de saída** personalizada
- [ ] Detecção automática do **FFmpeg** no sistema
- [ ] Arquivo `.env` para credenciais do Spotify
- [ ] Barra de progresso mais detalhada
- [ ] Histórico de downloads
- [ ] Suporte a mais plataformas (SoundCloud, Deezer)

---

## 📜 Licença

Este projeto é disponibilizado para **uso livre** com finalidade **educacional e pessoal**.

> ⚠️ O uso indevido do conteúdo baixado é de **total e exclusiva responsabilidade do usuário**.

---

<div align="center">

⭐ **Gostou do projeto?** Deixe uma estrela no repositório!  
🐛 Encontrou um bug? [Abra uma issue](https://github.com/seu-usuario/script_download_spotify_youtube/issues)!

</div>
