from collections import deque


class Stack():
    def __init__(self):
        self.container = deque()  # creating a deque object

    def push(self, element):
        self.container.append(element)  # this gonna add the element

    def get(self):  #this is return all element inside deque object
        l = []
        for element in self.container:
            l.append(element)
        return l

    def pop(self):
        self.container.pop()  # this re move last element inside the container

    def reverse_string(self, element):  # this gonna reverse_string
        if element[::-1] in self.container:
            return
        self.container.append(element[::-1])

    def get_length(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


if __name__ == '__main__':
    pass