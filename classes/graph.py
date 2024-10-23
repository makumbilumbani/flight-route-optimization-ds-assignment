from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # Adding a one-way directed edge from one node to another
    def add_route(self, u, v):
        self.graph[u].append(v)
    
    # Getting the reverse graph (for Kosaraju's second pass)
    def get_transpose(self):
        transpose_graph = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                transpose_graph.add_route(v, u)
        return transpose_graph
    
    # Depth First Search (DFS) for traversing the graph
    def dfs(self, v, visited, stack=None):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(v)

    # Method to get all airports (nodes) in the graph
    def get_all_airports(self):
        airports = set(self.graph.keys())
        for destinations in self.graph.values():
            airports.update(destinations)
        return airports