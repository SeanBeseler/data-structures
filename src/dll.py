class double_linked_list(object):
    def __init__(self):
        """initializes double linked list"""
        self.head = self
        self.tail = self
        self.next_node = None
        self.prev_node = None
        self.data = None
        self.size = 0

    def push(self, val):
        """creates new node, pushes it to top of linked list and makes it the head"""
        self.size += 1
        current = self.head
        new_dll = double_linked_list()
        new_dll.next_node = current
        new_dll.data = val
        current.prev_node = new_dll
        self.head = new_dll
        if self.tail.data is None:
            self.tail = self.head
            self.tail.next_node = None
        return self.head

    def append(self, val):
        """creates a new node, appends it to end of linked list and makes it the tail"""
        self.size += 1
        current = self.tail
        new_dll = double_linked_list()
        new_dll.prev_node = current
        new_dll.data = val
        current.next_node = new_dll
        self.tail = new_dll
        if self.head.data is None:
            self.head = self.tail
            self.head.prev_node = None
        return self.tail

    def pop(self):
        """
        Removes(pops) the head of the list and returns the node.
        New head is established.
        """
        current = self.head
        try:
            temp_data = current.data
            self.head = current.next_node
            if self.head is not None:
                self.head.prev_node = None
            elif temp_data is None:
                raise IndexError('Linked list is empty')
            self.size -= 1
            return temp_data
        except AttributeError:
            raise IndexError('Linked list is empty')

    def shift(self):
        """
        Removes(shifts) the tail of the list and returns the node.
        New tail is established.
        """
        current = self.tail
        try:
            temp_data = current.data
            self.tail = current.prev_node
            if self.tail is not None:
                self.tail.next_node = None
            elif temp_data is None:
                raise IndexError('Linked list is empty')
            self.size -= 1
            return temp_data
        except AttributeError:
            raise IndexError('linked list is empty')

    def remove(self, val):
        """removes a given node from the linked list"""
        current = self.head
        if val == current.data:
            self.size -= 1
            return self.head.pop()
        elif val == self.tail.data:
            self.size -= 1
            return self.tail.shift()
        while current.next_node is not None:
            current = current.next_node
            if current.data == val:
                current.next_node.prev_node = current.prev_node
                current.prev_node.next_node = current.next_node
                self.size -= 1
                return current.data
        raise IndexError('Not found in list')

    def __len__(self):
        """returns the length of the double linked list"""
        length = self.size
        return length
