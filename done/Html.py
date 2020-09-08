from bs4 import BeautifulSoup as bs
import pandas as pd
from os.path import exists
import os
from os import remove
from urllib.request import Request, urlopen
import urllib.error as ur  # import HTTPError
from requests import get as rget
import time
from progress.bar import IncrementalBar
import tqdm
import json
import csv

    
def convert_html(url):
    responce = rget(url, headers=hdr).text
    soup = bs(responce, features="lxml") 
    return soup

def getTitle(url):
    """Проверка ссылки на ошибки"""
    try:
        html = Request(url, headers=hdr)
        html = urlopen(html)
    except ur.HTTPError:  # если ошибка то выводим сообщение
        return "Http Error or Access denite"
    except ur.URLError:
        return "Bad Link"

