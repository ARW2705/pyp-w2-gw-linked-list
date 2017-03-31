from .interface import AbstractLinkedList
from .node import Node

'''
class LinkedListIterator(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start
        self.previous = None
        
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            self.previous = self.current
            self.current = self.current.next
            return self.previous

        
    next = __next__
'''

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = elements
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return "{}".format(self.elements if self.elements is not None else "[]")

    def __len__(self):
        return self.count()

    def __iter__(self):
        #return LinkedListIterator(self.start, self.end)
        current_node = self.start
        while current_node:
            yield current_node.elem
            current_node = current_node.next
        raise StopIteration

    def __getitem__(self, index):
        if not self:
            raise IndexError
        if index > len(self):
            raise IndexError
        index_count = 0
        for elem in self:
            if index_count == index:
                return elem
            index_count += 1

    def __add__(self, other):
        for elem in other:
            self.append(elem)
        return self

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self
        
    def __repr__(self):
        pass

    def __eq__(self, other):
        return (self.__repr__() == other.__repr__())
        
    def __ne__(self, other):
        return (self.__repr__() == other.__repr__())

    def append(self, element):
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
            self.end = self.start
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        count = 0
        for i in self:
            count += 1
        return count
        
    def pop(self, index=None):
        current_node = self.start
        previous_node = None
        count = 0
        if not self.count():
            raise IndexError
        if index is None:
            index = len(self) - 1
        if index >= self.count():
            raise IndexError
        while current_node:
            if index == 0:
                previous_node = current_node
                self.start = current_node.next
                return previous_node
            if count == index:
                previous_node.next = current_node.next
                return current_node
            count += 1
            previous_node = current_node
            current_node = current_node.next

    repr = __repr__
