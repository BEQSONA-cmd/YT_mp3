import yt_dlp
import os

def download_youtube_as_mp3(url, output_path="music/"):
    try:
        os.makedirs(output_path, exist_ok=True)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
        }

        print(f"Downloading: {url}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
            print(f"Downloaded as MP3: {filename}")
            return filename

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
video_url = "https://www.youtube.com/watch?v=qU9mHegkTc4&list=RDGMEM6ijAnFTG9nX1G-kbWBUCJAVMqU9mHegkTc4&start_radio=1"
download_youtube_as_mp3(video_url)