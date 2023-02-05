# <h1 align="center">📺  Youtube Video Downloader</h1>

<br>

## Usage in Terminal 💻: 
    python youtube_video_downloader.py [quality] [link]

## Example : 
    python youtube_video_downloader.py FHD https://www.youtube.com/watch?v=dQw4w9WgXcQ
<br>

    python youtube_video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
<br>

## ⭐ Quality arguments -
- For 4K quality use **4K / 2160p / UHD**
- For 2K quality use **2K / 1440p / QHD**
- For 1080 quality use **1K / 1080p / FHD**
- For 720p quality use **720p / HD**
- If no quality argument is passed then **720p is selected as Default**.

<br>

> Insert link in place of **[link]** in Terminal.

<br>

### 📄 It is a video downloader for YouTube created using pytube and some other libraries for downloading videos in mp4 format.
<br>
<br>

### ⚠ <mark>Before using the video downloader</mark> <br/>
* first install the necessary libraries by running in terminal the following commands:

    ```
    pip install youtube_downloader-2.0-py3-none-any.whl
    wheel unpack youtube_downloader-2.0-py3-none-any.whl
    ```
* **OR** manually install libraries by running
    ```
    pip install pytube moviepy wheel
    wheel unpack youtube_downloader-2.0-py3-none-any.whl
    ```
* Then changing directory to the python file
    ```
    cd .\youtube_downloader-2.0\youtube_downloader\
    ```
* Now you are ready to use the video downloader
<br><br>

> It can be used to download YouTube videos of 4K, 2K, 1080p, 720p size.<br>

> pytube and moviepy are dependency required.<br>

> To Batch install videos insert all links in 'links' list<br>

> Quality greater than 720p takes much more Time to download.<br>

> You can also use the YouTube_Downloader() function in your code by importing youtube_downloader package and calling the function<br>

> YouTube_Downloader() function takes 2 arguments first is link to video and second is quality of video.<br>

> URL of WHL file : https://github.com/rony0000013/youtube_downloader_full/blob/master/dist/youtube_downloader-2.0-py3-none-any.whl<br>

> URL of repository : https://github.com/rony0000013/youtube_downloader_full<br>
<br>
<br>
created by Rounak Sen
