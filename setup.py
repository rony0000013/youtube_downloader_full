from setuptools import setup, find_packages

setup(name='youtube_downloader',
      version='2.0',
      description='It is a video downloader for YouTube created using pytube and some other libraries for downloading videos in mp4 format.',
      url='https://github.com/rony0000013/Youtube-Video-Downloader',
      author='rony0000013',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pytube',
          'moviepy'
      ],
      zip_safe=False)