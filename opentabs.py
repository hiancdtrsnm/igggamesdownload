from selenium.webdriver import Chrome
import sys
import os
from fire import Fire
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from selenium.webdriver.common.keys import Keys
import re

url = 'https://igg-games.com/port-182013070-royale-3-gold-free-download.html'


def display_downloads(url):

    browser = Chrome()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    links = filter(lambda a: 'docs.google.com' in a.attrs.get(
        'href', ''), soup.find_all('a'))
    links = map(lambda link: 'https://' +
                re.findall(r'xurl=s://(.*)&', link.attrs['href']).pop(), links)
    links = list(links)

    for link in links:

        browser.get(link)

        browser.find_element_by_xpath('//*[@id="uc-download-link"]').click()
        browser.implicitly_wait(300)
        sleep(300)
    return links
    # while True:
    #     sleep(1)


if __name__ == '__main__':
    Fire(display_downloads)
