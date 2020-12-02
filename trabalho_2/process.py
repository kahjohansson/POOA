from abc import ABC, abstractmethod

class Processing(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def process(self):
        pass
