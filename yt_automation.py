import yt_dlp

def download_best_video_audio(link):
    """Download the best video and audio for a given link."""
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video + audio
        'merge_output_format': 'mp4',  # Merge into MP4 format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output file name
    }

    # Download video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([link])
            print(f"Downloaded: {link}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")

def process_links_from_file(file_path):
    """Process YouTube links from a text file and download each."""
    try:
        with open(file_path, 'r') as file:
            links = [line.strip() for line in file if line.strip()]  # Read non-empty lines

        if not links:
            print("No links found in the file.")
            return

        print(f"Found {len(links)} links. Starting downloads...")
        for idx, link in enumerate(links, start=1):
            print(f"\n[{idx}/{len(links)}] Downloading: {link}")
            download_best_video_audio(link)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error processing the file: {e}")

# Main script
if __name__ == "__main__":
    file_path = input("Enter the path to the text file containing YouTube links: ")
    process_links_from_file(file_path)
