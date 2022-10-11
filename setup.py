from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='spotify2youtube',
    version='1.0',
    description='An application that gets your Spotify songs and grabs the mp3 from YouTube',
    author='Stefan Heng',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)