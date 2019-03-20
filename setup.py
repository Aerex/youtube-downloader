from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='ytolibrary',
      version='0.0.4',
      description='Download youtube videos and upload to music library',
      long_description=readme,
      classifiers=[
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6"
      ],
      keywords = ['youtube', 'upload'],
      url='https://github.com/Aerex/youtube-downloader',
      author='Aerex',
      packages=['YoutubeDownloader', 'YoutubeDownloader.library', 'YoutubeDownloader.oauth'],
      install_requires=[
      	'validators',
        'pytube',
        'gmusicapi',
        'ffmpy',
        'oauth2client',
        'selenium'
      ],
      test_suite='pytest',
      tests_require=['pytest', 'pytest-mock','mock', 'coverage'],
      include_package_data=True,
      zip_safe=False)
