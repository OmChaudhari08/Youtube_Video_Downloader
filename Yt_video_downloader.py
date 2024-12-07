import yt_dlp

def download_best_video_audio(link):
    """Download the best video and audio for a given YouTube link."""
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video + audio
        'merge_output_format': 'mp4',  # Merge into MP4 format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output file name
    }

    try:
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print(f"Download completed: {link}")
    except Exception as e:
        print(f"Failed to download {link}: {e}")

# Main script
if __name__ == "__main__":
    link = input("Enter the YouTube link: ")
    if link.strip():
        download_best_video_audio(link.strip())
    else:
        print("No link provided. Exiting.")
