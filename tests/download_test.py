from YoutubeDownloader import YoutubeDownloader
import pytest
import mock
from pytest_mock import mocker
from pytube import YouTube

class mockVideo():
    def download(self, dir, on_finish=None):
        if on_finish:
            on_finish(dir)

def test_download(mocker):
    url = 'https://google.com'
    format = 'mp4'
    quality = '480p'
    dir = '/tmp/'
    mocker.patch.object(YouTube, '__init__')
    mocker.patch.object(YouTube, 'get')
    mocker.patch.object(mockVideo, 'download')

    YouTube.get.return_value = mockVideo()
    YouTube.__init__.return_value = None

    yt = YoutubeDownloader(url)
    yt.download(format, quality, dir)
    YouTube.get.assert_called_with(format, quality)
    args = mockVideo.download.call_args
    assert dir in args[0]
    assert yt.startDownloading == True






