from linked_list import LinkedList


class Stack(object):
    """Make a new class Stack from using methods from Linked List"""
    def __init__(self, data):
        self.newLinkedList = LinkedList(data)

    def pop(self):
        return self.newLinkedList.pop()

    def push(self, val):
        return self.newLinkedList.push(val)

    def __len__(self):
        return self.newLinkedList.__len__()
