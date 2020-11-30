import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, webpage):
        self.webpage = webpage 


    def get_pages(self, title=True, url=False):
        html_text = requests.get(self.webpage).text
        soup = BeautifulSoup(html_text, 'html.parser')
        data = {}

        if title:
            titles = soup.select('h2.c-main-headline__title')
            titles = titles + soup.select('h2.c-headline__title')
            data['title'] = titles

        print(data)
            