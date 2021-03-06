class Dque(object):
    """init the deque object"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.next_node = None
        self.pre_node = None
        self.value = None
        self.len = 0

    def append(self, val):
        """ append a new value to the tail of the dque"""
        new_dque = Dque()
        temp_node = self.tail
        if self.len == 0:
            self.head = new_dque
        else:
            self.tail.next_node = new_dque
            new_dque.pre_node = temp_node
        self.tail = new_dque
        self.tail.value = val
        self.len += 1

    def appendleft(self, val):
        """ appends a new value to the head of the dque"""
        new_dque = Dque()
        temp_node = self.head
        if self.len == 0:
            self.tail = new_dque
        else:
            self.head.pre_node = new_dque
            new_dque.next_node = temp_node
        self.head = new_dque
        self.head.value = val
        self.len += 1

    def pop(self):
        """ pops the tail"""
        if self.len == 0:
            raise IndexError
        current = self.tail
        self.tail = current.pre_node
        self.tail.next_node = None
        self.len -= 1
        return(current.value)

    def popleft(self):
        """pops the head"""
        if self.len == 0:
            raise IndexError
        current = self.head
        self.head = current.next_node
        self.head.pre_node = None
        self.len -= 1
        return(current.value)

    def peek(self):
        """looks at the value of the tail"""
        if self.len == 0:
            return None
        return self.tail.value

    def peekleft(self):
        """looks at the value of the head"""
        if self.len == 0:
            return None
        return self.head.value

    def size(self):
        """return the size of the dque"""
        return self.len
