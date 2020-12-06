# Trabalho proposto

Construir uma ferramenta para encontrar e baixar títulos das notícias do dia, nos principais sites de notícias (G1, UOL, etc).

Respeitando os dois primeiros conceitos SOLID:
* Princípio aberto-fechado
* Princípio da responsabilidade-única.

O projeto propôe encontrar e baixar títulos de notícias bem como seus respectivos links dos seguintes sites:
* [UOL Notícias](https://noticias.uol.com.br)
* [Folha de S. Paulo](https://www.folha.uol.com.br)
* [O Globo](https://oglobo.globo.com/)

Para isso utilizamos a biblioteca [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), que facilita a obtenção de informação a partir do HTML de páginas web.

Além de extrair os dados, os organizamos de duas formas: 
* Formato .csv utilizando o caractere `;` como separador.
* Filtro por palavra nos títulos.


## Pré Configuração.

Para que o projeto funcione corretamente é necessário a instalação de algumas bibliotecas e para isso, recomendamos o [pip](https://pip.pypa.io/en/stable/installing/)

[Python](https://www.python.org/downloads/)
```
    sudo apt install python3
```

[Beautiful Soup 4](https://pypi.org/project/bs4/)
```
    pip install bs4
```

[CSV](https://pypi.org/project/python-csv/)
```
    pip install python-csv
```  

## Como usar
Deixamos pré-configurado para executar todos os crawlers criados e ambos os processamentos, tanto para exportação em um .csv quanto o filtro por palavras. Portanto, para executar sem nenhuma mudança, basta usar:

```bash
    python3 __main__.py
```

Para alguma modificação, acesse o arquivo de configuração disponível em `config.yaml`. O arquivo de configuração possui o seguinte formato:
* `crawler`: Crawlers que devem ser executados.
* `processing`: Tipos de pós processamento que devem ser executados.
* `params`: Referente a classe `FilterNews`, contêm as palavras que devem ser buscadas em formato de lista.

```
crawler:
    - FolhaCrawler
    - UolCrawler

processing:
    - ExportCsv
    - FilterNews

params:
    FilterNews: [[covid, bolsonaro, câmara]]
        
```

## Alteração e criação

Encorajamos a criação de novas classes tanto para criar um crawler quanto para criar tipos de pós processamento! Para isso, siga os próximos passos.

Na estrutura do projeto, temos na raiz uma pasta para `crawler` e uma para `processing`, onde estão os arquivos e classes com suas respectivas funções.

### Para implementar um novo crawler, deve-se:

1. Criar um novo arquivo na pasta `crawler`.
2. Importar a classe pai, `Crawler`.

```py
from .crawler import Crawler
```

3. Criar uma classe com nome intuitivo filha da classe `Crawler`.

```py
class JornalZCrawler(Crawler):
```

4. Siga a mesma estrutura utilizada no método construtor __init__ do arquivo `folha_crawler.py`.

```py
def __init__(self):
        self.nome = 'Nome Do Jornal'
        self.url = 'https://exemplo.com.br'
```

5. Definir o método que irá efetivamente fazer o crawler como `get_data(self)`, que retorne uma lista.

```py
 def get_data(self):
    data = []

     '''          
        Code
    '''

    return data
```

Para criar um crawler do 0, recomendamos fortemente a documentação do [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) ou sua versão em [português](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/) 

### Para implementar um novo tipo de pós processamento, deve-se:
1. Criar um novo arquivo na pasta `processing`.
2. Importar a classe pai `Processing`.
``from .process import Processing``
3. Criar uma classe com nome intuitivo filha de `Processing`.

```
py
class BagOfWords(Processing):
```

4. Definir o método `process` que irá fazer o processamento desejado.
```
py
def process(self, <parâmetros>):
    '''
        code
    '''
```
5. Caso necessário, alterar a seção `params` no arquivo de configurações para que ela contenha o nome da classe seguida dos parâmetros utilizados.
```
params:
    BagOfWords: [[<parâmetros>]]
```


