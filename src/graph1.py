class Graph1(object):
    def __init__(self):
        """init the graph object"""
        self.graph = {}
        
    def add_node(self,val):
        """adds a node to the graph"""
        if self.graph.has_key(val):
            raise ValueError ('graph all ready has the node')
        self.graph[val] =[]
        
    def add_edges(self,val1,val2):
        """adds edges to the graph"""
        if not self.graph.has_key(val1):
            self.add_node(val1)
        if not self.graph.has_key(val2):
            self.add_node(val2)
        if val2 in self.graph[val1]:
            self.graph[val1].remove()
        self.graph[val1].append(val2)
            
    def del_node(self,val):
        """del node from graph and edges that are from or to node"""
        if self.graph.has_key(val):
            del self.graph[val]
            for key in self.graph:
                if val in self.graph[key]:
                    self.graph[key].remove()
        else:
            raise ValueError ('graph does has node')

    def del_edge(self,val1,val2):
        """del an edge"""
        if self.graph.has_key(val1) and self.graph.has_key(val2):
            raise ValueError('graph does not have one of the nodes')
        if not val2 in self.graph[val1]:
            raise ValueError('graph does not have edge')
        self.graph[val1].remove(val2)
        
    def has_node(self, val):
        """check to see if graph has node"""
        if self.graph.has_key(val):
            return True
        return False

    def edges(self):
        """ouputs all neighbors of val"""
        pair = ()
        output = []
        for key in self.graph:
            for neigh in self.graph[key]:
                pair = pair + (key , neigh)
                output.append(pair)
        return output
    
    def adjacent(self, val1 ,val2):
        """check tos see if val1 is adjacent to val2"""
        if self.graph.has_key[val1] and self.graph.has_key[val2]:
            raise ValueError ('graph does not have one of the nodes')
        if val2 in self.graph[val1]:
            return True
        return False
    
    def neighbors(self, val):
        """ouputs all neighbors of val"""
        pair = ()
        output = []
            for neigh in self.graph[key]:
                pair = pair + (key , neigh)
                output.append(pair)
        return output

    def nodes(self):
        output = []
        for key in self.graph:
            output.append(key)
        return output
            

    
        

    

