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

    def get_short_path(self, start, end, li):
        """Retrieves shortest path between nodes."""
        path = []
        while True:
            path.append(end)
            if end is start:
                break
            end = li[end][1]
        return path

    def bellman_ford_helper(self, li, start):
        """Bellman-Ford helper, iterates through graph."""
        for key in li:
            for key2 in self.graph[key]:
                # import pdb; pdb.set_trace()
                if li[key2[0]][0] > li[key][0] + key2[1] and key2[0] != start:
                    new_value = li[key][0] + key2[1]
                    li[key2[0]] = (new_value, key)
        return li

    def bellman_ford(self, start, end):
        """Implementation of Bellman-Ford algorithm."""
        nodes = self.nodes()
        li = {}
        for x in nodes:
            if x == start:
                li[x] = (0, x)
            else:
                li[x] = (float('inf'), 'nan')
        temp_li = self.bellman_ford_helper(li, start)
        while True:
            if temp_li == li:
                return self.get_short_path(start, end, li)
            li = temp_li
            temp_li = self.bellman_ford_helper(li, start)
        return self.get_short_path(start, end, li)

    def dijkstra(self, start, end):
        """Implentation of Dijkstra's algorithm."""
        nodes = self.nodes()
        nodes.remove(start)
        potential_nodes = {}
        for x in nodes:
            potential_nodes[x] = (float('inf'), 'nan')
        li = {}
        li[start] = (0, start)
        for x in self.graph[start]:
            potential_nodes[x[0]] = (x[1], start)
        while True:
            if len(potential_nodes) == 0:
                return self.get_short_path(start, end, li)
            min_node = float('inf')
            min_node_name = ''
            for x in potential_nodes:
                if potential_nodes[x][0] < min_node:
                    min_node = potential_nodes[x][0]
                    min_node_name = x
            for x in self.graph[min_node_name]:
                if potential_nodes[x[0]][0] > x[1] + min_node:
                    potential_nodes[x[0]] = (x[1] + min_node, potential_nodes[x[0]][0])
            li[min_node_name] = (min_node, start)
            potential_nodes.remove(min_node_name)
            start = min_node_name
