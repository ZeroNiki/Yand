import argparse

from src.yandex import get_yandex_track
from src.yt import yt_search
from src.dw import download_music, downlad_cover
from src.lyrics import get_lyric
from src.mtd_mp3 import change_cover, change_metadata

from src.config import FULL_DIR

def parse_argument():
    parse = argparse.ArgumentParser(description="Yand")
    parse.add_argument("url", help="Url from yandex track")
    args = parse.parse_args()

    return args


def main():
    url = parse_argument() 
    results = get_yandex_track(url.url)

    author = results[0]
    clear_author = author.replace('&', '')

    track_name = results[1]
    cover_url = results[2]

    keyword = clear_author + " " + track_name
    file_name = f'{clear_author} {track_name}.mp3'
    cover_name = f'{clear_author} {track_name}.jpg'

    link = yt_search(keyword) 

    download_music(link, clear_author, track_name)
    downlad_cover(clear_author, track_name, FULL_DIR, cover_url)

    lyric = get_lyric(track_name, clear_author)

    change_metadata(f"{FULL_DIR}{file_name}", clear_author, track_name, lyric)
    change_cover(f"{FULL_DIR}{file_name}", f"{FULL_DIR}{cover_name}")
    
