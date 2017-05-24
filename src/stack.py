from linked_list import LinkedList


class Stack(object):
    def __init__(self, data):
        self.newLinkedList = LinkedList(data)

    def pop(self):
        return self.newLinkedList.pop()

    def push(self, val):
        return self.newLinkedList.push(val)

    def __len__(self):
        return self.newLinkedList.__len__()


st = Stack([1, 2, 3])
st.push(5)
print(st.pop())
