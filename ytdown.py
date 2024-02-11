from pytube import YouTube, Playlist

def download_video(yt):
    print(f"\nTitle: {yt.title}")
    print(f"Views: {yt.views}")

    available_streams = yt.streams.filter(progressive=True)
    resolutions = {stream.resolution for stream in available_streams if stream.resolution}
    print("\nAvailable Resolutions:")
    for i, resolution in enumerate(resolutions, 1):
        print(f"{i}. {resolution}")

    choice = get_user_choice(len(resolutions))
    selected_resolution = list(resolutions)[choice - 1]
    yd = yt.streams.filter(res=selected_resolution, progressive=True).first()

    yd.download("D:/YouTube Downloader/Video")#Seect Ur Video download path
    print("\nYour file has been downloaded successfully.")

def download_audio(yt):
    print(f"\nTitle: {yt.title}")
    print(f"Views: {yt.views}")

    yd = yt.streams.filter(only_audio=True).first()

    yd.download("D:/YouTube Downloader/Audio")#Seect Ur Audio download path
    print("\nYour audio file has been downloaded successfully.")

def download_playlist(pl):
    print(f"\nDownloading playlist: {pl.title}")
    for video in pl.video_urls:
        try:
            yt = YouTube(video)
            download_video(yt)
        except Exception as e:
            print(f"Error downloading video {video}: {str(e)}")

def get_user_choice(max_value):
    while True:
        try:
            choice = int(input("Enter the number corresponding to your desired resolution: "))
            if 1 <= choice <= max_value:
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("-----------------------------")
    print("Youtube Downloader by CHXRITH")
    print("-----------------------------")

    while True:
        link_type = input("\nEnter 'V' for single video, 'A' for audio, or 'P' for playlist: ").strip().lower()
        if link_type == 'v':
            link = input("Enter link of YouTube Video: ")
            try:
                yt = YouTube(link)
                download_video(yt)
            except Exception as e:
                print(f"Error downloading video: {str(e)}")
        elif link_type == 'a':
            link = input("Enter link of YouTube Video: ")
            try:
                yt = YouTube(link)
                download_audio(yt)
            except Exception as e:
                print(f"Error downloading audio: {str(e)}")
        elif link_type == 'p':
            link = input("Enter link of YouTube Playlist: ")
            try:
                pl = Playlist(link)
                download_playlist(pl)
            except Exception as e:
                print(f"Error downloading playlist: {str(e)}")
        else:
            print("Invalid choice. Please enter 'V', 'A', or 'P'.")

        choice = input("Do you want to download another video or playlist? (Y/N): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
