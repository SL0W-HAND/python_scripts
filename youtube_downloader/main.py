from pytube import YouTube
from pytube import Stream
from pytube import Playlist
from tqdm import tqdm
import os

## function to download video
def video_downloader():
    option = int(input("""how do you want to download it?: 
    1. Download video with link
    2. Download from a list of links
    3. Download a playlist
    4. Exit
    """))
    
    def download_video(link):
        # function to update progress bar
        def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
            pbar.update(len(data_chunk))
        
        yt = YouTube(link, on_progress_callback=progress_callback)
        ys = yt.streams.get_highest_resolution()

        print(f"""
        Downloading: {yt.title},
        duration: {yt.length} seconds
        """)
        # download and show progress bar
        pbar = tqdm(total=ys.filesize, unit="bytes")
        
        ys.download('./Video_Downloads')
    
    if option == 1:
        link = input("Enter the link: ")
        download_video(link)
        print("Video downloaded")

    if option == 2:
        file = open("links.txt", "r", encoding="utf-8")
        for line in file:
            download_video(line)
            print("##################################################")
        file.close()
        print("done")

    if option == 3:
        playlist_url = input("Enter the playlist url: ")
        playlist = Playlist(playlist_url)
        for video in playlist.video_urls:
            download_video(video)
            print("##################################################")
        print("done")
        
    if option == 4:
        print("Exiting")
        exit()

## function to download audio
def audio_downloader():
    option = int(input("""how do you want to download it?: 
    1. Download audio with link
    2. Download from a list of links
    3. Download a playlist
    4. Exit
    """))

    def download_audio(link):
        # function to update progress bar
        def progress_bar(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
            pbar.update(len(data_chunk))
        
        yt = YouTube(link,on_progress_callback=progress_bar)
        #download in mp3 format
        ys = yt.streams.get_audio_only()
        print(f"""
        Downloading: {yt.title},
        duration: {yt.length} seconds
        """)
        # download and show progress bar
        pbar = tqdm(total=ys.filesize, unit="bytes")
        #convert file to mp3
        out_file = ys.download('./Audio_Downloads')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    if option == 1:
        link = input("Enter the link: ")
        download_audio(link)
        print("Audio downloaded")

    if option == 2:
        file = open("links.txt", "r", encoding="utf-8")
        for line in file:
            download_audio(line)
            print("##################################################")
        file.close()
        print("done")

    if option == 3:
        playlist_url = input("Enter the playlist url: ")
        playlist = Playlist(playlist_url)
        for video in playlist.video_urls:
            download_audio(video)
            print("##################################################")
        print("done")

    if option == 4:
        print("Exiting")
        exit()
    
def main():
    option = int(input("""Enter the option:
    1. Download video
    2. Download audio
    3. Exit
    """))
    if option == 1:
        video_downloader()
    if option == 2:
        audio_downloader()
    if option == 3:
        print("Exiting")
        exit()
    
if __name__ == '__main__':
    main()