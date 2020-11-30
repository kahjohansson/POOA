from crawler import Crawler
import requests
from bs4 import BeautifulSoup

class FolhaCrawler(Crawler):

    def get_data(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
            
        titles = soup.find_all('h2', class_='c-main-headline__title')
        titles = titles + soup.find_all('h2', class_='c-headline__title')
        
        for t in titles:
            t = t.get_text()
            data.append(t)            

        return data