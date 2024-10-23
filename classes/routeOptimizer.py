from collections import defaultdict
from classes.sccFinder import SCCFinder

# The purpose of this Class tis to handle the optimization of flight routes
class RouteOptimizer:
    def __init__(self, graph, starting_airport):
        self.graph = graph
        self.starting_airport = starting_airport
        self.scc_finder = SCCFinder(graph)
        self.sccs = self.scc_finder.find_sccs()
    
    # Function to compress the graph into SCCs and find additional routes
    def minimum_additional_routes(self):
        # Step 1: Building the compressed graph (SCCs as nodes)
        scc_map = {}
        scc_graph = defaultdict(set)
        
        # print("Strongly Connected Components (SCCs):")
        for idx, scc in enumerate(self.sccs):
            # print(f"SCC {idx}: {scc}")
            for airport in scc:
                scc_map[airport] = idx
        
        # Step 2: Adding SCC-to-SCC edges in compressed graph
        for u in self.graph.graph:
            for v in self.graph.graph[u]:
                if scc_map[u] != scc_map[v]:
                    scc_graph[scc_map[u]].add(scc_map[v])
        
        # Step 3: Counting SCCs with in-degree 0 (no incoming edges)
        in_degrees = defaultdict(int)
        for u in scc_graph:
            for v in scc_graph[u]:
                in_degrees[v] += 1
        
        # Step 4: Counting how many SCCs have in-degree 0, excluding the one containing the starting airport
        start_scc = scc_map[self.starting_airport]
        zero_in_degree_count = sum(1 for i in range(len(self.sccs)) if i != start_scc and in_degrees[i] == 0)
        
        return zero_in_degree_count