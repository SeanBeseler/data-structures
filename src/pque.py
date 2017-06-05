class Pque(object):
    """make as priority queue  priority scale is 0 through -99
        0 has greatest priority with ties being first come first pop"""
    def __init__(self):
        self.next_node = None
        self.priority = 0
        self.value = None
        self.tail = None
        self.head = None
        self.size = 0
        
    def insert(self,value , priority = -99):
        """ inserts a value into the que defalt priority is -99"""
        new_pque = Pque()
        new_pque.priority = priority
        if self.size is 0:
            self.head = new_pque
            self.tail = new_pque
        else:
            current_node = self.head
            pre_node = None
            for x in range(self.size):
                if new_pque.priority > current_node.priority:
                    if current_node is self.head:
                        new_pque.next_node = self.head
                        self.head = new_pque
                        break
                    else:
                        pre_node.next_node = new_pque
                        new_pque.next_node = current_node
                        self.size += 1
                        new_pque.value = value
                        break
                if current_node is self.tail:
                    self.tail.next_node = new_pque
                    self.tail = new_pque
                    break
                else:
                    pre_node = current_node
                    current_node = current_node.next_node
        self.size += 1
        new_pque.value = value
    def peek(self):
        """returns the data in the head of the pque with out removing it"""
        if self.head is None:
            raise IndexError ('que is empty')
        return self.head.value
    
    def pop(self):
        """returns the data in the head of pque and removes it """
        if self.head is None:
            raise IndexError ('que is empty')
        temp_val = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return temp_val
                    
                
            
        
