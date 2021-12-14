## Implementing LIFO stack class

class Stack:

    def __init__(self):
        self.__container = []

    # Container should only be changed due to class methods
    @property
    def container(self):
        return self.__container

    def push(self, element):
        self.__container.append(element)

    def pop(self):
        if len(self.__container) < 1:
            raise IndexError("Can't pop from an empty stack. Please push elements first!")
        else:
            return self.__container.pop()

    def peek(self):
        if len(self.__container) < 1:
            raise IndexError("Cant show last element of the stack because there are no elements!")
        else:
            return self.__container[-1]

    def getSize(self):
        return len(self.__container)
