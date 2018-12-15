# Pravljenje apstraktnih klasa:
# https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod


# Najčešće operacije sa stablom:
# https://en.wikipedia.org/wiki/Tree_(data_structure)#Common_operations
class Tree(ABC):

    class Node(ABC):

        # Podrazumijevani parametar: nema roditelja (korijen)
        def __init__(self, key, parent=None):
            self.__key = key
            self.__parent = parent

        def get_key(self):
            return self.__key

        def has_parent(self):
            return self.__parent is not None

        def get_parent(self):
            return self.__parent

        @abstractmethod
        def has_children(self):
            pass

        @abstractmethod
        def get_children(self):
            pass

        @abstractmethod
        def get_siblings(self):
            pass

    def __init__(self):
        self.__root = None

    @abstractmethod
    def add(self, key):
        pass

    @abstractmethod
    def add_to_parent(self, key, parent):
        pass

    @abstractmethod
    def find(self, key):
        pass

    def find_parent_of(self, key):
        return self.find(key).get_parent()

    def find_siblings_of(self, key):
        self.find(key).get_siblings()

    @abstractmethod
    def remove(self, key):
        pass

    def get_root(self):
        return self.__root

    def is_empty(self):
        return self.__root is None

    @staticmethod
    def is_root(node):
        return not node.has_parent()

    @staticmethod
    def is_leaf(node):
        return not node.has_children()
