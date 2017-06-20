class Graph3(object):
    def __init__(self, itt=0):
        """init the graph object"""
        self.graph = {}

    def add_node(self, val):
        """adds a node to the graph"""
        if val in self.graph:
            raise ValueError('graph all ready has the node')
        self.graph[val] = []

    def add_edge(self, val1, val2, weight):
        """adds edges to the graph"""
        if val1 not in self.graph:
            self.add_node(val1)
        if val2 not in self.graph:
            self.add_node(val2)
        self.graph[val1].append((val2, weight))

    def del_node(self, val):
        """del node from graph and edges that are from or to node"""
        if val in self.graph:
            del self.graph[val]
            for key in self.graph:
                for x in range(len(self.graph[key])):
                    if val in self.graph[key][x]:
                        del self.graph[key][x]
        else:
            raise ValueError('graph does has node')

    def del_edge(self, val1, val2):
        """del an edge"""
        flag = 0
        locations = []
        if val1 not in self.graph or val2 not in self.graph:
            raise ValueError('graph does not have one of the nodes')
        for x in range(len(self.graph[val1])):
            if val2 in self.graph[val1][x]:
                locations.append(x)
                flag = 1
        for x in locations:
            del self.graph[val1][x]
        if flag == 0:
            raise ValueError('graph does not have edge')

    def has_node(self, val):
        """check to see if graph has node"""
        if val in self.graph:
            return True
        return False

    def edges(self):
        """ouputs all neighbors of val"""
        output = []
        for key in self.graph:
            for neigh in self.graph[key]:
                pair = (key, neigh[0])
                output.append(pair)
        return output

    def adjacent(self, val1, val2):
        """Check to see if val1 is adjacent to val2"""
        if val1 not in self.graph or val2 not in self.graph:
            raise ValueError('graph does not have one of the nodes')
        for x in self.graph[val1]:
            if val2 in x:
                return True
        return False

    def neighbors(self, val):
        """Outputs all neighbors of val"""
        output = []
        for neigh in self.graph[val]:
            output.append(neigh[0])
        return output

    def nodes(self):
        """Returns a list of all nodes in graphs"""
        output = []
        for key in self.graph:
            output.append(key)
        return output

    def depth_first_traversal(self, val1, output=[]):
        """Retrieves nodes ordered by a depth search criteria"""
        if val1 not in self.graph:
            raise ValueError('This node is not in the graph')
        neighbors = []
        for x in self.graph[val1]:
            neighbors.append(x[0])
        if val1 not in output:
            output = []
            output.append(val1)
        for x in range(len(neighbors)):
            if neighbors[x] not in output:
                output.append(neighbors[x])
                output = self.depth_first_traversal(neighbors[x], output)
        return output

    def breadth_first_traversal(self, val):
        """Retrieves nodes ordered by a breadth search criteria"""
        output = []
        done = False
        if val not in self.graph:
            raise ValueError('This node is not in the graph')
        output.append(val)
        iterator = 0
        while not done:
            neighbors = []
            for x in self.graph[val]:
                neighbors.append(x[0])
            sample_size = len(output)
            for x in range(len(neighbors)):
                if neighbors[x] not in output:
                    output.append(neighbors[x])
            if sample_size == len(output) and iterator >= len(output) - 1:
                done = True
            else:
                iterator += 1
                val = output[iterator]
        return output
