from pytube import YouTube
import os
from ffmpy import FFmpeg
import subprocess
import validators
from subprocess import call

class YoutubeDownloader(object):

    def __init__(self, url):
        if not validators.url(url):
            raise StandardError('{0} is not a valid url'.format(url))
        self.yt = YouTube(url)

    def __getVideoQuality(self, ext, quality):
        if not self.yt:
            raise StandardError('Youtube is not defined')

        if quality != "lowest" and quality != "highest":
            print 'Using invalid quality default to lowest'
            quality = "lowest"

        videos = self.yt.filter(ext)

        highestresolution = 0
        lowestresolution = 90000

        for video in videos:
            resolution = int(video.resolution.replace("p", ""))
            if quality == 'highest' and resolution > highestresolution:
                highestresolution = resolution
                continue
            elif quality == 'lowest' and resolution < lowestresolution:
                lowestresolution = resolution
                continue
        return lowestresolution if quality == 'lowest' else highestresolution

    def download(self, ext, quality, directory, callback=None):
        validYoutubeTypes = ['mp4']
        if not self.yt:
            raise StandardError('YouTube is not defined')

        if not callback:
            raise StandardError('Callback needs to be set')

        if ext in validYoutubeTypes:
            resolution = str(self.__getVideoQuality(ext, quality)) + 'p'
            video = self.yt.get(ext, resolution)

            if directory[len(directory)-1] == '/':
                directory = directory[0:len(directory)-1]

            if not os.path.exists('{0}/{1}.{2}'.format(directory, video.filename, ext)):
                video.download(directory, on_finish=callback)
            else:
                callback('{0}/{1}.{2}'.format(directory, video.filename, ext))
        else:
            raise StandardError('{0} is not a valid download media type')

    def convert(self, path, filename, ext):
        if not path:
            raise StandardError('path is not defined')
        if not os.path.exists('{0}/{1}.mp3'.format(path, filename)):
            ff = FFmpeg(
                inputs={'{0}/{1}.{2}'.format(path, filename, ext): None},
                outputs={'{0}/{1}.mp3'.format(path, filename): ['-vn', '-acodec', 'libmp3lame', '-ac', '2', '-ab', '160k',
                                                                '-ar', '48000']}
                )
            print ff.cmd

            stderr = ff.run(stderr=subprocess.PIPE)
            if stderr:
                print stderr

    def clean(self, path):
        path  = path.strip('/')
        if os.path.exists(path):
            call(['rm', '-rf', '{0}/*'.format(path)])


    def upload(self, library=None, path='', match=False):
        if not library:
            raise StandardError('library module is not defined')
        library.upload(path, match)






