import yt_dlp


class DownloadService:
    def __init__(self, save_path='music/'):
        self.path = save_path

    def download_audio_as_mp3(self, video_url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': self.path + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
            'ffmpeg_location': r'C:\Users\berna\OneDrive\Desktop\Elective\ffmpeg-master-latest-win64-gpl\bin',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            try:
                ydl.download([video_url])
                return True
            except Exception as e:
                print(f"Download failed: {e}")
                return False





