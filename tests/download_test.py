from YoutubeDownloader import YoutubeDownloader
import pytest
import os
import mock
from pytest_mock import mocker
from pytube import YouTube

def mockCallback(path):
    pass
class mockVideo(object):
    def __init__(self, filename, resolution):
        self.filename = filename
        self.resolution = resolution
    def download(self, dir, on_finish=None):
        if on_finish:
            on_finish(dir)

def test_download_highest_quality(mocker):
    highest = '1080p'
    videos = []
    videosConfig = [
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
    for x in range(3):
        videos.append(mockVideo(videosConfig[x]['filename'], videosConfig[x]['resolution']))

    print 'hello\n'
    print videosConfig[0]['filename']
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
    os.path.exists.assert_called_with('{0}/{1}.{2}'.format(dir, videos[0].filename, ext))

def test_download_lowest_quality(mocker):
    lowest = '480p'
    videos = []
    videosConfig = [
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


    for x in range(3):
        videos.append(mockVideo(videosConfig[x]['filename'], videosConfig[x]['resolution']))

    url = 'https://google.com'
    ext = 'mp4'
    quality = 'lowest'
    dir = '/tmp'
    mocker.patch.object(YouTube, '__init__')
    mocker.patch('os.path.exists')
    mocker.patch.object(YouTube, 'get')
    mocker.patch.object(YouTube, 'filter')
    mocker.patch.object(mockVideo, 'download')

    YouTube.get.return_value = videos[2]
    YouTube.__init__.return_value = None
    YouTube.filter.return_value = videos
    os.path.exists.return_value = True

    yt = YoutubeDownloader(url)
    yt.download(ext, quality, dir, callback=mockCallback)
    YouTube.get.assert_called_with(ext, lowest)
    os.path.exists.assert_called_with('{0}/{1}.{2}'.format(dir, videosConfig[2]['filename'], ext))








