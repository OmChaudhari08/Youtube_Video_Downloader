import yt_dlp

def get_video_links_by_range(playlist_url, start, end):
    """Extract video links from a playlist based on the range of playlist numbers."""
    ydl_opts = {
        'extract_flat': True,  # Do not download, only retrieve metadata
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist = ydl.extract_info(playlist_url, download=False)
        
        if 'entries' not in playlist:
            print("No entries found in the playlist.")
            return []

        # Filter videos based on the playlist index
        selected_videos = playlist['entries'][start - 1:end]
        
        # Extract URLs
        video_links = [f"https://www.youtube.com/watch?v={video['id']}" for video in selected_videos if video.get('id')]
        return video_links

# Main logic
if __name__ == "__main__":
    playlist_url = "https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA"
    start = 70
    end = 150
    
    video_links = get_video_links_by_range(playlist_url, start, end)
    if video_links:
        print(f"Found {len(video_links)} videos in the specified range:")
        for link in video_links:
            print(link)
    else:
        print("No videos found in the specified range.")
