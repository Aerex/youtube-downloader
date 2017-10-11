from YoutubeDownloader import YoutubeDownloader
import pytest
import os
import mock
from pytest_mock import mocker
from pytube import YouTube

def mockCallback(path):
    pass
class mockVideo():
    def download(self, dir, on_finish=None):
        if on_finish:
            on_finish(dir)

def test_download_highest_quality(mocker):
    highest = '1080p'
    videos = [
        {
            'resolution': '1080p',
            'filename': 'sample.mp4'
        },
        {
            'resolution': '720p',
            'filename': 'sample.mp4'
        },
        {
            'resolution': '480p',
            'filename': 'sample.mp4'
        }
    ]

    url = 'https://google.com'
    ext = 'mp4'
    quality = 'highest'
    dir = '/tmp'
    mocker.patch.object(YouTube, '__init__')
    mocker.patch('os.path.exists')
    mocker.patch.object(YouTube, 'get')
    mocker.patch.object(YouTube, 'filter')
    mocker.patch.object(mockVideo, 'download')

    YouTube.get.return_value = videos[0]
    YouTube.__init__.return_value = None
    YouTube.filter.return_value = videos
    os.path.exists.return_value = True

    yt = YoutubeDownloader(url)
    yt.download(ext, quality, dir, callback=mockCallback)
    YouTube.get.assert_called_with(ext, highest)
    os.path.exists.assert_called_with('{0}/{1}.{2}'.format(dir, videos[0]['filename'], ext))








