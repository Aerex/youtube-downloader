from YoutubeDownloader import YoutubeDownloader
import pytest
import mock
from pytest_mock import mocker
from pytube import YouTube

def test_init(mocker):
    mocker.patch.object(YouTube, '__init__')
    YouTube.__init__.return_value = None
    url = 'https://google.com'
    yt = YoutubeDownloader(url)
    YouTube.__init__.assert_called_with(url)

def test_fail_init(mocker):
    url = 'notavalidurl'
    mocker.patch.object(YouTube, '__init__')
    with pytest.raises(StandardError, match=r'is not a valid url'):
        yt = YoutubeDownloader(url)





