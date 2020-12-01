from crawler import Crawler
import requests
from bs4 import BeautifulSoup


class UolCrawler(Crawler):

    def __init__(self):
        self.nome = 'UOL Notícias'
        self.url = 'https://noticias.uol.com.br/'

    def get_data(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
            
        
        crawled = soup.find_all('div', class_='thumbnails-wrapper')
        
        for c in crawled:
            url = c.find('a')['href']
            title = c.find('h3').get_text() 
            if title is not None:
                data.append((title,url))  
             
        return data        
 
   