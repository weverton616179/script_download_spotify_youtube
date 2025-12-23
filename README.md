# 🎬 Downloader de Vídeos e Músicas (YouTube & Spotify)

Um **script em Python** para baixar **vídeos, áudios e playlists do YouTube** e **músicas/playlists do Spotify**, com escolha de **qualidade** e **formato** diretamente pelo **terminal**.

> Projeto focado em simplicidade, controle total pelo usuário e uso educacional.

---

## ✨ Funcionalidades

### ✅ YouTube

* 📹 Baixar **vídeos** ou **playlists**
* 🎚️ Escolher resolução (**2160p até 144p**)
* 📦 Escolher formato de vídeo (**mp4, mkv, webm**)
* 🎧 Baixar **apenas áudio**
* 🔊 Escolher qualidade do áudio (**96kbps até 320kbps**)
* 🎼 Escolher formato de áudio (**mp3, m4a, wav, flac, opus, etc.**)

### ✅ Spotify

* 🎵 Baixar **músicas** ou **playlists**
* 🎚️ Escolher formato do áudio
* 📝 Nome automático dos arquivos:

  ```
  Artista - Música.ext
  ```

---

## 🧠 Tecnologias Utilizadas

* **yt-dlp** → downloads do YouTube
* **spotDL** → downloads de músicas do Spotify (via YouTube)
* **FFmpeg** → conversão e junção de áudio/vídeo

---

## 📁 Estrutura do Projeto

```text
projeto/
└── baixar_video.py
```

---

## 🧰 Requisitos

### 🔹 Python

* **Versão:** 3.9 ou superior

Verifique com:

```bash
python --version
```

---

### 🔹 FFmpeg (OBRIGATÓRIO)

O FFmpeg é usado para **converter** e **juntar** áudio/vídeo.

#### 🪟 Windows

1. Baixe o arquivo `ffmpeg-git-essentials.7z` em:

   * [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extraia e **adicione o ffmpeg ao PATH** do sistema
3. Teste no terminal:

```bash
ffmpeg -version
```

#### 🐧 Linux (Debian / Ubuntu)

```bash
sudo apt install ffmpeg
```

---

## 📦 Instalação das Dependências

Instale as bibliotecas Python necessárias:

```bash
pip install yt-dlp spotdl
```

---

## 🔐 Configuração do Spotify (IMPORTANTE)

Para baixar músicas do Spotify, é necessário configurar a **API oficial do Spotify**.

### 1️⃣ Criar um App no Spotify Developer

1. Acesse:

   * [https://developer.spotify.com/](https://developer.spotify.com/)
2. Crie um novo app
3. Copie as credenciais:

   * `CLIENT_ID`
   * `CLIENT_SECRET`

---

### 2️⃣ Configurar no Código

No arquivo `baixar_video.py`, edite:

```python
spotdl = Spotdl(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    downloader_settings=downloader_options
)
```

➡️ Substitua pelos seus dados reais.

---

## ▶️ Como Usar

Execute o script no terminal:

```bash
python baixar_video.py
```

Você verá o menu:

```text
-------------- Downloader de vídeos, músicas e playlists --------------
Escolha uma opção:
1 - Baixar vídeos do YouTube
2 - Baixar áudios do YouTube
3 - Baixar músicas do Spotify
```

---

## 🎥 Opção 1 — Baixar Vídeos do YouTube

1. Cole o link do **vídeo** ou **playlist**
2. Escolha a **qualidade** (ex: `1080p`)
3. Escolha o **formato** (`mp4`, `mkv` ou `webm`)

📌 Se a qualidade escolhida não existir, o script baixa automaticamente a **melhor disponível**.

---

## 🎧 Opção 2 — Baixar Áudio do YouTube

1. Cole o link do vídeo ou playlist
2. Escolha a **qualidade do áudio**
3. Escolha o **formato** (`mp3`, `flac`, `opus`, etc.)

O áudio será **extraído e convertido automaticamente**.

---

## 🎵 Opção 3 — Baixar Músicas do Spotify

1. Cole o link da **música** ou **playlist** do Spotify
2. Escolha o **formato do áudio**

📌 As músicas são buscadas no YouTube e baixadas automaticamente.

---

## 📂 Organização dos Arquivos

### YouTube

```text
01 - Nome do Vídeo.mp4
02 - Outro Vídeo.mkv
```

### Spotify

```text
Artista - Música.mp3
```

---

## ⚠️ Observações Importantes

* ❌ O script **não burla DRM**
* 📡 Downloads dependem da **disponibilidade pública** do conteúdo
* 🎓 Use apenas para **uso pessoal e educacional**
* ⏳ Playlists grandes podem demorar mais tempo

---

## 🚀 Possíveis Melhorias Futuras

* Interface gráfica (**GUI**)
* Downloads em **paralelo**
* Escolha de **pasta de saída**
* Detecção automática do **FFmpeg**
* Uso de arquivo `.env` para credenciais do Spotify

---

## 📜 Licença

Este projeto é de **uso livre** para fins **educacionais e pessoais**.

O uso indevido do conteúdo baixado é de **total responsabilidade do usuário**.

---

⭐ Se este projeto te ajudou, considere deixar uma estrela no repositório!
