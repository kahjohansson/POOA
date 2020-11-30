from abc import ABC, abstractmethod

class Crawler(ABC):

    def __init__(self, name, url):
        self.name = name
        self.url = url

    @abstractmethod
    def get_data(self):
        pass
        
            