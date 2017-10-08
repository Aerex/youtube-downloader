from pytube import YouTube
import validators

class YoutubeDownloader(object):
    validYoutubeTypes = ['mp4']
    def __init__(self, url):
        if not validators.url(url):
            raise StandardError('{0} is not a valid url'.format(url))
        self.yt = YouTube(url)
        self.startDownloading = False
        self.doneDownloading = False

    def download(self, ext, quality, directory):
        self.startDownloading = True
        def callback(path):
            print 'Downloaded to {0}'.format(path)
            self.doneDownloading = True
            self.startDownloading = False
        if not self.yt:
            raise StandardError('YouTube is not defined')

        if ext in self.validYoutubeTypes:
            video = self.yt.get(ext, quality)
            video.download(directory, on_finish=callback)
        else:
            raise StandardError('{0} is not a valid download media type')




