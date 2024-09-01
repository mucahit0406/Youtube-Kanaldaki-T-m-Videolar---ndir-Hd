import os
import subprocess
import yt_dlp as youtube_dl


import subprocess

ffmpeg_path = r"C:\ffmpeg\ffmpeg.exe"  # ffmpeg'in tam yolu
try:
    subprocess.run([ffmpeg_path, "-version"], check=True)
    print("FFmpeg is installed and ready to use.")
except subprocess.CalledProcessError:
    print("FFmpeg çalıştırılamadı. Lütfen ffmpeg yolunu ve kurulumunu kontrol edin.")
    exit(1)
except FileNotFoundError:
    print("FFmpeg bulunamadı. Lütfen ffmpeg yolunu ve kurulumunu kontrol edin.")
    exit(1)

# "indirilenler" adlı klasörü oluşturur (eğer yoksa)
os.makedirs('indirilenler', exist_ok=True)

ydl_opts = {
    'outtmpl': 'indirilenler/%(title)s.%(ext)s',  # İndirilen videolar bu klasöre kaydedilecek
    'format': 'bestvideo+bestaudio/best',  # En iyi video ve ses kalitesini indirip birleştirir
    'merge_output_format': 'mp4',  # Video ve ses dosyalarını birleştirir (genellikle mp4 formatında)
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Çıktı formatı
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["Bu kısma kanal linkini giriniz"])
