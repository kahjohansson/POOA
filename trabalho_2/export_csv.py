from process import Processing
import csv


class ExportCsv(Processing):

    def __init__(self, nome_site, news):
        self.nome_site = nome_site
        self.news = news

    def process(self):
        
        #Escrita csv utf8 pra ler no vscode, latin1 pro excell.
        output_path = 'output/' + self.nome_site + '.csv'
        with open(output_path, 'w+', encoding='utf8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["title", "url"])
            for title, url in self.news:
                writer.writerow([title,url])
