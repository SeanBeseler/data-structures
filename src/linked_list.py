class LinkedList(self, data):
    self.data = data

    def push(self, val):

    def pop(self):

    def size(self):
        current = self
        count = 1
        while current.next_node:
            count += 1
            current = current.next_node
        return count

    def search(self, val):
        current = self
        while current.next_node:
            if current.data == val:
                return current
            else:
                current = current.next_node
        raise Exception('Value does not exist in Linked List')

    def remove(self, node):
        current = self
        previouscurrent = ''
        while current.next_node:
            previouscurrent = current
            if current == node:
                previouscurrent.data = current.next_node.data
                previouscurrent.next_node = current.next_node.next_node
            current == current.next_node
        raise Exception('Node does not exist in Linked List')

    def display(self):
        current = self
        output = ''
        while current.next_node:
            output += current.data
            current = current.next_node
        return output
