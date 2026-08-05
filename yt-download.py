from pathlib import Path
from pytubefix import YouTube

try:
    vid_url = input("Enter the YouTube video URL: ").strip()
    vid_dir = Path.home() / "Desktop" / "messy-folder"

    yt = YouTube(vid_url)
    stream = yt.streams.get_highest_resolution()

    if stream is None: raise RuntimeError("No downloadable video stream was found.")

    stream.download(output_path=str(vid_dir))

    print(f"Download completed: {vid_dir}")
 
except Exception as e: print(f"Download failed: {e}")