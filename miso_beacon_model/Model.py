from abc import ABC, abstractmethod


class Model(metaclass=ABC):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.components = []

    @abstractmethod
    def getname(self):
        return self.name

    @abstractmethod
    def setname(self, name):
        self.name = name

    @abstractmethod
    def addcomponent(self, component):
        self.components = component

    @abstractmethod
    def getcomponents(self):
        return self.components
