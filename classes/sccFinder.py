from collections import defaultdict
# Class specifically to find SCCs using Kosaraju's Algorithm
class SCCFinder:
    def __init__(self, graph):
        self.graph = graph
        self.sccs = []
    
    # using Kosaraju's Algorithm to find all SCCs in 3 steps
    def find_sccs(self):
        visited = defaultdict(bool)
        stack = []

        # Step 1: Filling stack with nodes in decreasing finish time
        nodes = list(self.graph.graph.keys())
        for node in nodes:
            if not visited[node]:
                self.graph.dfs(node, visited, stack)

        # Step 2: Getting the transpose graph
        transpose_graph = self.graph.get_transpose()

        # Step 3: Processing all nodes in order of decreasing finish time
        visited = defaultdict(bool)
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transpose_graph.dfs(node, visited, component)
                self.sccs.append(component)
        return self.sccs