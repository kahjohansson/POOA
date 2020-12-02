#encoding: utf-8

from crawler.folha_crawler import FolhaCrawler
from crawler.globo_crawler import GloboCrawler
from crawler.uol_crawler import UolCrawler
from processing.export_csv import ExportCsv
import yaml



def get_config():
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        return config['crawler'], config['processing']


def main():
    crawlers, processings = get_config()

    if crawlers is not None:
        for crawler in crawlers:
            c = eval(crawler)()
            news = c.get_data()

            if processings is not None:
                for processing in processings:
                    p = eval(processing)(c.nome, news)
                    p.process()
            

if __name__ == "__main__":
    main()
