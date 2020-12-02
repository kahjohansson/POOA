from crawler import Crawler
import requests
from bs4 import BeautifulSoup

class GloboCrawler(Crawler):
	
	def __init__(self):
		self.nome = 'Globo Notícias'
		self.url = 'https://www.globo.com/'
		
	def get_data(self):
		html_text = requests.get(self.url).text
		soup = BeautifulSoup(html_text, 'html.parser', from_encoding="utf-8")
		data = []

		crawled = soup.find_all('div', class_='hui-premium')

		for c in crawled:
			url = c.find('a')['href']
			title = c.find('p').get_text()
			if title is not None:
				data.append((title,url))
		
		return data
