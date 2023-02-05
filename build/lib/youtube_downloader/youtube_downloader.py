from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from sys import argv
import os
from pathlib import Path


# To change download location feel free to change below
path_to_download_folder_video = str(os.path.join(Path.home(), r'Downloads\tmp\video'))
path_to_download_folder_audio = str(os.path.join(Path.home(), r'Downloads\tmp\audio'))
path_to_download_folder_Complete_video = str(os.path.join(Path.home(), r'Downloads\video'))


# For Batch download insert all links in string type in list below.
links = []

'''
                        📺  Youtube Video Downloader

    Usage in Terminal 💻: python youtube_video_downloader.py [quality] [link]

    Example : python youtube_video_downloader.py FHD https://www.youtube.com/watch?v=dQw4w9WgXcQ

              python youtube_video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

    ⭐ Quality arguments -
        > For 4K quality use 4K / 2160p / UHD
        > For 2K quality use 2K / 1440p / QHD
        > For 1080 quality use 1K / 1080p / FHD
        > For 720p quality use 720p / HD
        > If no quality argument is passed then 720p is selected as Default.

    > Insert link in place of [link] in Terminal.

    📄 It is a video downloader for YouTube created using pytube and some other libraries for downloading videos in mp4 format.

    ⚠ Before using the video downloader 
    > first install the necessary libraries by running in terminal the following commands:
        pip install youtube_downloader-2.0-py3-none-any.whl
        wheel unpack youtube_downloader-2.0-py3-none-any.whl

    > OR manually install libraries by running

        pip install pytube moviepy wheel
        wheel unpack youtube_downloader-2.0-py3-none-any.whl

    > Then changing directory to the python file

        cd .\youtube_downloader-2.0\youtube_downloader\

    > Now you are ready to use the video downloader
    
    > It can be used to download YouTube videos of 4K, 2K, 1080p, 720p size.
    > pytube and moviepy are dependency required.
    > To Batch install videos insert all links in 'links' list
    > Quality greater than 720p takes much more Time to download.
    > You can also use the YouTube_Downloader() function in your code by importing youtube_downloader package and calling the function
    > YouTube_Downloader() function takes 2 arguments first is link to video and second is quality of video.
    > URL of WHL file : https://github.com/rony0000013/youtube_downloader_full/blob/master/dist/youtube_downloader-2.0-py3-none-any.whl
    > URL of repository : https://github.com/rony0000013/youtube_downloader_full

    created by Rounak Sen
'''


# Check if optional arguments are specified
if len(argv) == 3:
    quality = argv[1]
    link = argv[2]
elif len(argv) == 2:
    link = argv[1]
else:
    link = None

print(quality, link)


# Fuction to check the Quality availability of the video
def quality_checker(link, quality="720p"):

    # youtube object
    yt = YouTube(link)

    if (quality == "4K" or quality == "UHD" or quality == "2160p") and yt.streams.filter(res="2160p", mime_type="video/webm"):
        return int(yt.streams.filter(res="2160p", mime_type="video/webm")[0].itag)
    elif (quality == "2K" or quality == "QHD" or quality == "1440p") and yt.streams.filter(res="1440p", mime_type="video/webm"):
        return int(yt.streams.filter(res="1440p", mime_type="video/webm")[0].itag)
    elif (quality == "1K" or quality == "FHD" or quality == "1080p") and yt.streams.filter(res="1080p", mime_type="video/webm"):
        return int(yt.streams.filter(res="1080p", mime_type="video/webm")[0].itag)
    elif (quality == "720p" or quality == "HD") and yt.streams.filter(res="720p", mime_type="video/mp4", progressive=True):
        return True
    else:
        print(f"Quality '{quality}' is not available for video -> {yt.title}")
        return False
    

    
# YouTube video download function
def YouTube_Downloader(link, quality="720p"):
    
    # Checking if link exists
    if link is None:
        print("😞 No link was provided so no video downloaded.")
        return False

    # youtube object
    yt = YouTube(link)

    # Getting Title of the video
    title = yt.title.replace(":", "")
    print("Title =", title)


    # creating empty video tag
    tag = quality_checker(link, quality)

    # If no quality is specified then download the video at default quality of 720p
    if tag == True:
        print("Downloading... ⏳⌛⏳⌛")
        yd = yt.streams.get_highest_resolution()
        yd.download(path_to_download_folder_Complete_video)
        print("🙂 Completed download. Enjoy. 😎")


    # if a tag was obtained, download the video
    if type(tag) == int:
        print("Downloading... ⏳⌛⏳⌛")

        # get the video stream
        yd_v = yt.streams.get_by_itag(tag)

        # download the video without audio and storing the video location in the variable
        video_loc = yd_v.download(path_to_download_folder_video)

        # ----------------------------------------------------------------

        # download the audio only of good quality
        yd_m = yt.streams.get_by_itag(int(yt.streams.filter(abr="160kbps", mime_type="audio/webm")[0].itag))
        if not yd_m:
            yd_m = yt.streams.get_by_itag(int(yt.streams.filter(abr="128kbps", mime_type="audio/mp4")[0].itag))

        # get the audio stream and storing the video location in the variable
        audio_loc = yd_m.download(path_to_download_folder_audio)

        # ----------------------------------------------------------------

        # If Folder is absent, then create a new folder
        if not os.path.isdir(path_to_download_folder_Complete_video):
            os.mkdir(path_to_download_folder_Complete_video)

        # Setting the output video location
        output_file = f"{path_to_download_folder_Complete_video}\{title}.mp4"

        # ----------------------------------------------------------------

        # creating video and audio objects
        clip = VideoFileClip(video_loc)
        audio_clip = AudioFileClip(audio_loc)
        # Joining video and audio files together
        video_clip = clip.set_audio(audio_clip)

        # Saving video in the folder
        video_clip.write_videofile(output_file)

        os.remove(video_loc)
        os.remove(audio_loc)
        print("🙂 Completed download. Enjoy. 😎")



YouTube_Downloader(link, quality)

# Batch downloading videos
if links != []:
    for l in links:
        YouTube_Downloader(l, quality)

