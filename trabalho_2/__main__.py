#encoding: utf-8

from folha_crawler import FolhaCrawler
from globo_crawler import GloboCrawler
from uol_crawler import UolCrawler
import yaml
import csv



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
                    eval(processing)()

    #Escrita csv utf8 pra ler no vscode, latin1 pro excell.
    
    with open('teste.csv', 'w', encoding='utf8', newline='') as file:
    
        writer = csv.writer(file)
        
        writer.writerow(["titulo", "link"])
        for tupla in news:
           writer.writerow([tupla[0],tupla[1]])
            

if __name__ == "__main__":
    main()
