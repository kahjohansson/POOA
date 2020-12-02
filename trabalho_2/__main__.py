from folha_crawler import FolhaCrawler
from globo_crawler import GloboCrawler
from uol_crawler import UolCrawler
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
                    eval(processing)()
        print(news)


if __name__ == "__main__":
    main()
