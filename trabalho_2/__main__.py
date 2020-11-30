from crawler import Crawler
from webpage import Webpage

g1 = Webpage('G1', 'https://g1.globo.com/')
crawler = Crawler(g1.homepage)
crawler.get_pages()

folha = Webpage('Folha', 'https://www.folha.uol.com.br/')
c = Crawler(folha.homepage)
c.get_pages()
