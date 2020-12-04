#encoding: utf-8

from crawler.folha_crawler import FolhaCrawler
from crawler.oglobo_crawler import OGloboCrawler
from crawler.uol_crawler import UolCrawler
from processing.export_csv import ExportCsv
from processing.filter_news import FilterNews
import yaml


def get_config():
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        return config['crawler'], config['processing'], config['params']


def main():
    crawlers, processings, params = get_config()

    if crawlers is not None:
        for crawler in crawlers:
            c = eval(crawler)()
            news = c.get_data()

            if processings is not None:
                for processing in processings:
                    p = eval(processing)(c.nome, news)
                    if processing in params and params[processing] is not None:
                        p.process(*params[processing])
                        
                    else:
                        p.process()
            

if __name__ == "__main__":
    main()
