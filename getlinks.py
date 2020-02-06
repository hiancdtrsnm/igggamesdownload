from parsel import Selector
import requests
import sys
from fire import Fire

base_url = 'https://drive.google.com'

def clean_url(url):

    if 'bluemediafiles' in url:
        separator = 'xurl=s'
        index = url.find(separator)

        url = 'https' + url[index + len(separator):]

    return url


def get_links(url):
    r = requests.get(url)

    html = Selector(text=r.text)
    all_href = html.xpath('//a/@href').getall()


    return [clean_url(href) for href in all_href if 'drive.google.com' in href]


def get_direct_download(url):
    xpath_selector = '//*[@id="uc-download-link"]/@href'

    ans = []

    for file in get_links(url):
        response = requests.get(file)

        html = Selector(text=response.text)

        href = html.xpath(xpath_selector).get()

        ans.append(base_url + href)

    return ans


if __name__ == "__main__":
    Fire(get_links)