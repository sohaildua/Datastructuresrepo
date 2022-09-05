from email.policy import default
import pprint
from collections import defaultdict
class Graph(object):
    
    def __init__(self,connections,size,directed=False):
        self._graph =defaultdict(set)
        self._directed =directed
        self.add_connections(connections)
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        
    
    def __len__(self):
        self.size
        
    #add edges
    def add_edge(self,v1,v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
     # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print
    
    def add_connections(self,connections):
        
        for node1,node2 in connections:
            self.add(node1,node2)
            
    def add(self,node1,node2):
        
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)
            
    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass
        
        
    
    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2,path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node  not in path:
                new_path = self.find_path(node, node2,path)
                if new_path:
                    return new_path
                
        return None
    

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                   ('C', 'D'), ('E', 'F'), ('F', 'C')]
g = Graph(connections,len(connections),directed=True)
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(g._graph)
print(g.find_path('A', 'C') )  

print(g.print_matrix)

