from folha_crawler import FolhaCrawler

cr = FolhaCrawler('Folha', 'https://www.folha.uol.com.br/')
news = cr.get_data()
