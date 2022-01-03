import requests
from bs4 import BeautifulSoup


def crawl_request(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup
