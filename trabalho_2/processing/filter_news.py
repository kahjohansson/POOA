from .process import Processing


class FilterNews(Processing):

    def __init__(self, nome_site, news):
        self.nome_site = nome_site
        self.news = news

    def process(self, words):
        print(f'---------------------{self.nome_site}---------------------\n')
        for w in words:
            w = w.lower()
            print(f'------------{w}------------\n')
            for n, u in self.news:
                if w in n.lower():
                    print(f'{n}')
                    print(f'{u}\n')


            