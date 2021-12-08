from pytube import YouTube
from pytube import Stream
from tqdm import tqdm


def main():
    option = int(input("""Enter the option: 
    1. Download video with link
    2. Download from a list of links
    3. Exit
    """))
    def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
        pbar.update(len(data_chunk))

    if option == 1:
        link = input("Enter the link: ")
        yt = YouTube(link, on_progress_callback=progress_callback)
        ys = yt.streams.get_highest_resolution()
        print(f"""
        Downloading: {yt.title},
        duration: {yt.length} seconds
        """)
        pbar = tqdm(total=ys.filesize, unit="bytes")
        # download and show progress bar
        ys.download()
        print("Video downloaded")
    if option == 2:
        file = open("links.txt", "r", encoding="utf-8")
        for line in file:
            yt = YouTube(line, on_progress_callback=progress_callback)
            ys = yt.streams.get_highest_resolution()
            print(f"""
            Downloading: {yt.title},
            duration: {yt.length} seconds
            """)
            pbar = tqdm(total=ys.filesize, unit="bytes")
            ys.download()
            print("##################################################")
        file.close()
        print("done")
    if option == 3:
        exit()

if __name__ == '__main__':
    main()