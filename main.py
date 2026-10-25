import os
import yt_dlp
import imageio_ffmpeg

# Enables ANSI color support in Windows CMD
os.system('')

class Cor:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    CIANO = '\033[96m'
    MAGENTA = '\033[95m'
    AZUL = '\033[94m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

def identificar_plataforma(url):
    url_lower = url.lower()
    if 'youtube.com' in url_lower or 'youtu.be' in url_lower:
        return f"{Cor.VERMELHO}YouTube{Cor.RESET}"
    elif 'instagram.com' in url_lower:
        return f"{Cor.MAGENTA}Instagram{Cor.RESET}"
    elif 'twitter.com' in url_lower or 'x.com' in url_lower:
        return f"{Cor.AZUL}Twitter / X{Cor.RESET}"
    else:
        return f"{Cor.CIANO}Other Platform{Cor.RESET}"

def baixar_midia(url, formato_escolhido):
    caminho_ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    pasta_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    opcoes = {
        'outtmpl': os.path.join(pasta_downloads, '%(title).100B [%(id)s].%(ext)s'),
        'noplaylist': True,
        'ffmpeg_location': caminho_ffmpeg,
        'windowsfilenames': True,
    }

    # Checks if a cookies.txt file exists in the same folder as the script
    caminho_cookies = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cookies.txt')
    if os.path.exists(caminho_cookies):
        opcoes['cookiefile'] = caminho_cookies
        print(f"{Cor.VERDE}[i] cookies.txt file detected! Authentication enabled.{Cor.RESET}")
    elif 'instagram.com' in url.lower() or 'x.com' in url.lower() or 'twitter.com' in url.lower():
        print(f"{Cor.AMARELO}[!] Warning: 'cookies.txt' not found in the script folder.{Cor.RESET}")
        print(f"{Cor.AMARELO}    If Instagram/Twitter blocks the download, please add the cookies.txt file.{Cor.RESET}")

    plataforma = identificar_plataforma(url)

    if formato_escolhido == '1':
        opcoes['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best[ext=mp4]/best'
        opcoes['merge_output_format'] = 'mp4'
        print(f"\n{Cor.CIANO}Detected platform:{Cor.RESET} {Cor.NEGRITO}{plataforma}{Cor.RESET}")
        print(f"{Cor.CIANO}Starting {Cor.NEGRITO}MP4 VIDEO{Cor.RESET}{Cor.CIANO} download to:{Cor.RESET} {pasta_downloads}")

    elif formato_escolhido == '2':
        opcoes['format'] = 'bestaudio/best'
        opcoes['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
        print(f"\n{Cor.CIANO}Detected platform:{Cor.RESET} {Cor.NEGRITO}{plataforma}{Cor.RESET}")
        print(f"{Cor.CIANO}Starting {Cor.NEGRITO}MP3 AUDIO{Cor.RESET}{Cor.CIANO} download to:{Cor.RESET} {pasta_downloads}")

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print(f"\n{Cor.VERDE}{Cor.NEGRITO}✔ Download completed successfully!{Cor.RESET} Saved to: {Cor.AMARELO}{pasta_downloads}{Cor.RESET}")
    except Exception as e:
        print(f"\n{Cor.VERMELHO}{Cor.NEGRITO}✖ An error occurred during download:{Cor.RESET} {e}")

if __name__ == '__main__':
    print(f"{Cor.MAGENTA}Luqueta Codes© - All rights reserved{Cor.RESET}")
    print(f"{Cor.CIANO}============================================================{Cor.RESET}")
    print(f"{Cor.NEGRITO}               WELCOME TO RIPPER CONVERTER                  {Cor.RESET}")
    print(f"             {Cor.VERMELHO}YouTube{Cor.RESET} | {Cor.MAGENTA}Instagram{Cor.RESET} | {Cor.AZUL}Twitter (X){Cor.RESET}")
    print(f"{Cor.CIANO}============================================================{Cor.RESET}")

    while True:
        print(f"\n{Cor.AMARELO}[Tip: Type '0' or 'exit' at any time to close]{Cor.RESET}")
        link = input(f"{Cor.NEGRITO}Paste the link here (YouTube, Instagram, or Twitter/X): {Cor.RESET}").strip()

        if link.lower() in ['0', 'exit', 'quit', 'sair']:
            print(f"\n{Cor.CIANO}Closing program... See you later!{Cor.RESET}")
            break

        if link:
            print(f"\n{Cor.NEGRITO}Select the desired format:{Cor.RESET}")
            print(f"{Cor.VERDE}[1]{Cor.RESET} Video ({Cor.CIANO}High Quality MP4{Cor.RESET})")
            print(f"{Cor.VERDE}[2]{Cor.RESET} Audio Only ({Cor.CIANO}MP3{Cor.RESET})")
            print(f"{Cor.VERMELHO}[0]{Cor.RESET} Cancel / Exit")

            escolha = input(f"\n{Cor.NEGRITO}Enter 1, 2, or 0: {Cor.RESET}").strip()

            if escolha in ['1', '2']:
                baixar_midia(link, escolha)
                print(f"\n{Cor.CIANO}------------------------------------------------------------{Cor.RESET}")
            elif escolha == '0':
                print(f"\n{Cor.CIANO}Closing program... See you later!{Cor.RESET}")
                break
            else:
                print(f"\n{Cor.VERMELHO}Invalid option! Please choose only 1, 2, or 0.{Cor.RESET}")
        else:
            print(f"\n{Cor.VERMELHO}No valid link entered. Please try again.{Cor.RESET}")
