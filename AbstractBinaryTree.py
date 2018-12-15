# Pravljenje apstraktnih klasa:
# https://docs.python.org/3/library/abc.html
from abc import abstractmethod
# Ne treba nam abc.ABC jer je naslijeđivanje tranzitivno.
from AbstractTree import Tree


class BinaryTree(Tree):

    class Node(Tree.Node):

        def __init__(self, key, parent):
            super(BinaryTree.Node, self).__init__(key, parent)
            self.__left = None
            self.__right = None

        def get_left(self):
            return self.__left

        def get_right(self):
            return self.__right

        def has_children(self):
            return self.__left is not None or self.__right is not None

        @abstractmethod
        def get_children(self):
            pass

        # Gets only one sibling.
        def get_siblings(self):
            if self.__parent is None:
                return None
            else:
                return self.__parent.__right if self.__parent.__left is self else self.__parent.__left

    @abstractmethod
    def add(self, key):
        pass

    @abstractmethod
    def add_to_parent(self, key, parent):
        pass

    @abstractmethod
    def find(self, key):
        pass

    @abstractmethod
    def remove(self, key):
        pass
