class our_queue(object):
    def __init__(self):
        """initializes queue"""
        self.head = self
        self.tail = self
        self.next_node = None
        self.data = None
        self.size = 0

    def enqueue(self, val):
        """creates new node, pushes it to bottom of the queue and makes it the tail"""
        self.size += 1
        new_qu = our_queue()
        if self.head.data is None:
            self.head = new_qu
            self.head.next_node = None
        else:
            self.tail.next_node = new_qu
        new_qu.data = val
        self.tail = new_qu
        return self.head


    def dequeue(self):
        """
        Removes the head of the queue and returns the value.
        New head is established.
        """
        current = self.head
        temp_data = None
        try:
            temp_data = current.data
            if temp_data is None:
                raise IndexError('que is empty')
            self.head = current.next_node
            self.size -= 1
            return temp_data
        except AttributeError:
            raise IndexError('que is empyt')

    def peek(self):
        """
         peeks at the data of the head
        """
        current = self.head
        temp_data = None
        try:
            temp_data = current.data
            if temp_data is None:
                raise IndexError('que is empty')
            return temp_data
        except AttributeError:
                raise IndexError('que is empty')


    def __len__(self):
        """returns the length of the double linked list"""
        length = self.size
        return length
temp = our_queue()
temp.enqueue(4)
temp.enqueue(3)
print(len(temp))
