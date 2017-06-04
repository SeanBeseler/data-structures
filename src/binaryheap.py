
class binary_heap(object):
    def __init__(self):
        self.size = 0
        self.list = []

    def _get_parent(self, position):
        if position % 2 == 1:
            position -= 1
        parent_position = position/2
        return parent_position

    def _check_heap_after_push(self):
        for x in range(self.size -1):
            current_position = self.size - x -1
            #if current_position < 3:
            if self.list[current_position] < self.list[self._get_parent(current_position)]:
                temp_var = self.list[current_position]
                self.list[current_position] = self.list[self._get_parent(current_position)]
                self.list[self._get_parent(current_position)] = temp_var
            """else:
                partent1 = 0
                partent2 = 0
                if self._get_parent(current_position) %2 == 0:
                    partent1 = self._get_parent(current_position) -1
                    partent2 = self._get_parent(current_position)
                else:
                    partent1 = self._get_parent(current_position) 
                    partent2 = self._get_parent(current_position) + 1
                    
                if partent1 > partent2:
                    if self.list[current_position] < self.list[partent1]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[partent1]
                        self.list[partent1] = temp_var
                else:
                    if self.list[current_position] < self.list[partent2]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[partent2]
                        self.list[partent2] = temp_var"""
                    
    def push(self,val):
        if val not in self.list:
            self.list.append(val)
            self.size += 1
            self._check_heap_after_push()
            
    def _check_heap_after_pop(self):
        for x in range(self.size -1):
            if x + 2 < self.size:
                if self.list[x] > self.list[(x*2)+ 1] or self.list[x] > self.list[(x*2) + 2]:
                    if self.list[(x*2)+1] < self.list[(x*2)+2]:
                        temp_var = self.list[x]
                        self.list[x] = self.list[x+1]
                        self.list[x+1] = temp_var
                    else:
                        temp_var = self.list[x]
                        self.list[x] = self.list[x+2]
                        self.list[x+2] = temp_var
            
                        
                elif self.list[x] > self.list[x+1]:
                        temp_var = self.list[x]
                        self.list[x] = self.list[x+1]
                        self.list[x+1] = temp_var

    def pop(self):
        tem_var = self.list[0]
        self.list[0] = self.list[self.size -1]
        self.list[self.size -1] = tem_var
        self.list.remove(tem_var)
        self.size -= 1
        self._check_heap_after_pop()
        return tem_var
    
bh = binary_heap()
bh.push(13)
print(bh.list)
bh.push(9)
print(bh.list)
bh.push(15)
print(bh.list)
bh.push(12)
print(bh.list)
bh.push(11)
print(bh.list)
bh.push(14)
print(bh.list)
bh.push(11.1)
print(bh.list)
print(bh.pop())
print(bh.list)
print(bh.pop())
print(bh.list)
print(bh.pop())
print(bh.list)
print(bh.pop())
print(bh.list)
print(bh.pop())
print(bh.list)
print(bh.pop())

                   
