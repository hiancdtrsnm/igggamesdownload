from parsel import Selector
import requests
import sys
from pprint import pp

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


if __name__ == "__main__":
    pp(get_links(sys.argv[1]))