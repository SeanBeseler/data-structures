class LinkedList(object):
    
    def __init__(self, data):
        self.data = None
        self.next_node = None
        self.head = self
        flag = 0
        if type(data) == list or type(data) == tuple:
            for x in range(len(data)):
                if flag ==0:
                    self.data = data[x]
                    self.next_node = None
                    flag =1
                
                else:
                    self.push(data[x])
        else:
            self.data = data
    def push(self, val):
        current = self.head
        newl = LinkedList(val)
        newl.next_node = current
        self.head = newl
        return self

    def pop(self):
        current = self.head
        flag = 1
        try:
            tem_data = current.data
            self.head = current.next_node
            return tem_data
        except AttributeError:
            flag = 0
        raise IndexError ('linked list is empty')

    def size(self):
        current = self.head
        count = 1
        while current.next_node:
            count += 1
            current = current.next_node
        return count

    def search(self, val):
        current = self.head
        while current.next_node != None:
            if current.data == val:
                return current
            else:
                current = current.next_node
        if current.data == val:
            return current
        else:
            current = current.next_node
        raise Exception('Value does not exist in Linked List')

    def remove(self, node):
        current = self.head
        previouscurrent = None
        while current.next_node is not None:
            if current == node:
                previouscurrent.next_node = current.next_node
                return
            else:
                previouscurrent = current
                current = current.next_node
            
        raise Exception('Node does not exist in Linked List')

    def display(self):
        current = self.head
        output = ''
        while current.next_node != None:
            output += str(current.data) + ', '
            current = current.next_node
        output += str(current.data)
        return output
new = LinkedList([1,2,3])
new.remove(new.search(2))
print(new.display())


