from selenium.webdriver import Chrome
import sys
import os
from fire import Fire
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from selenium.webdriver.common.keys import Keys
import re
from furl import furl
import requests


class GameNotFound(Exception):
    pass

url = 'https://igg-games.com/port-182013070-royale-3-gold-free-download.html'


def display_downloads(url):

    browser = Chrome()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    links = filter(lambda a: 'google.com' in a.attrs.get(
        'href', ''), soup.find_all('a'))
    clean_links = []
    for link in links:
        params = furl(link.attrs['href']).args
        if 'xurl' in params:
            lk = 'http'+params['xurl']
            clean_links.append(lk)
    links = list(clean_links)
    #print(links)
    for link in links:

        if '/file/d' in link:
            id_re = 'file/d/([^//]+)/'
            print(link)
            id = re.findall(id_re, link).pop()
            link = f'https://drive.google.com/uc?id={id}&export=download'

        print(link)
        r = requests.get(links)
        if r.status_code >= 400:
            raise GameNotFound('Game not found in '+link)
        browser.get(link)
        browser.find_element_by_xpath('//*[@id="uc-download-link"]').click()
        browser.implicitly_wait(300)
        sleep(300)

    return links
    # while True:
    #     sleep(1)


if __name__ == '__main__':
    Fire(display_downloads)

#display_downloads('https://igg-games.com/xcom-2-war-chosen-pc-game-166215494-cracked-free-download.html')