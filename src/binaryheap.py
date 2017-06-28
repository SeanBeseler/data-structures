class Binary_heap(object):
    def __init__(self, val=None):
        """init binary heap and checks val"""
        self.size = 0
        self.list = []
        if type(val) in [list, tuple]:
            for x in val:
                self.push(x)

    def _get_parent(self, position):
        """returns the parent of the position"""
        position -= 1
        parent_position = int(position/2)
        return parent_position

    def _get_left_kid(self, position):
        """gets the left kid for a position"""
        position = (position * 2) + 1
        if position > self.size - 1:
            return None
        return position

    def _get_right_kid(self, position):
        """gets the right kid for a position"""
        position = (position + 1) * 2
        if position > self.size - 1:
            return None
        return position

    def _check_heap_after_push(self):
        """gets the left kid for a position"""
        for x in range(self.size - 1):
            current_position = self.size - x - 1
            if self.list[current_position] < self.list[self._get_parent(current_position)]:
                temp_var = self.list[current_position]
                self.list[current_position] = self.list[self._get_parent(current_position)]
                self.list[self._get_parent(current_position)] = temp_var

    def push(self, val):
        """push a val on to the list"""
        if val not in self.list:
            self.list.append(val)
            self.size += 1
            self._check_heap_after_push()
        else:
            raise ValueError('number in heap already')

    def _check_heap_after_pop(self):
        """sorts the hep after a pop"""
        for x in range(self.size - 1):
            current_position = x
            right_kid = self._get_right_kid(current_position)
            left_kid = self._get_left_kid(current_position)
            if right_kid is not None or left_kid is not None:
                if right_kid is None:
                    if self.list[left_kid] < self.list[current_position]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[left_kid]
                        self.list[left_kid] = temp_var
                elif left_kid is None:
                    if self.list[right_kid] < self.list[current_position]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[right_kid]
                        self.list[right_kid] = temp_var
                else:
                    if self.list[left_kid] < self.list[current_position] and self.list[left_kid] < self.list[right_kid]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[left_kid]
                        self.list[left_kid] = temp_var
                    elif self.list[right_kid] < self.list[current_position] and self.list[left_kid] > self.list[right_kid]:
                        temp_var = self.list[current_position]
                        self.list[current_position] = self.list[right_kid]
                        self.list[right_kid] = temp_var

    def pop(self):
        """pop the lowest value off"""
        if self.size > 0:
            tem_var = self.list[0]
            self.list[0] = self.list[self.size - 1]
            self.list[self.size - 1] = tem_var
            self.list.remove(tem_var)
            self.size -= 1
            self._check_heap_after_pop()
            return tem_var
        return None
