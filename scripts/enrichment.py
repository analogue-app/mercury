import requests
from bs4 import BeautifulSoup, SoupStrainer
from fetch_spotify import spotify_get
from fetch_imdb import *
from fetch_goodreads import *
from fetch_artsy import *
from typing import Dict
from constants import APIs

def get_url(url: str) -> str:
    url = url.split('/')
    
    if 'http' in url[0]:
        site_name = url[2]

    else:
        site_name = url[0]

    return site_name

def enrich_test(url: str) -> Dict:
    site_name = get_url(url)
    enrich_data = {}

    if site_name in APIs:

        if site_name == "www.goodreads.com" or site_name == "goodreads.com":
            enrich_data = fetch_goodreads(url)

        elif site_name == "www.imdb.com" or site_name == "imdb.com":
            enrich_data = fetch_imdb(url)

        elif site_name == "open.spotify.com":
            enrich_data = spotify_get(url)

        elif site_name == "www.artsy.net" or site_name == "artsy.net":
            enrich_data = fetch_artsy(url)

    return enrich_data
