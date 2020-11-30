from crawler import Crawler
import requests
from bs4 import BeautifulSoup

class FolhaCrawler(Crawler):

    def get_data(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
            
        crawled = soup.find_all('a', class_='c-main-headline__url')
        crawled = crawled + soup.find_all('a', class_='c-headline__url')
        
        for c in crawled:
            url = c['href']
            title = c.find('h2')
            if title is not None:
                title = title.get_text()
                data.append((title,url))            

        return data