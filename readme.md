# Flight Route Optimizer

## Project Overview

This project is designed to optimize flight routes between a set of airports. Given a list of airports and one-way flight routes between them, the goal is to calculate the minimum number of additional one-way routes required to ensure that every airport is reachable from a given starting airport.

### Key Features:

- **Graph Data Structure**: A directed graph is used to represent the airports and the flight routes between them.
- **Strongly Connected Components (SCC)**: The graph is divided into strongly connected components to identify clusters of airports that can be reached from one another.
- **Kosaraju's Algorithm**: This algorithm is used to find the strongly connected components efficiently.
- **Minimum Route Calculation**: Once the graph is compressed based on the SCCs, the program calculates the minimum additional routes needed to connect all components to the starting airport.

## Algorithm: Kosaraju's Algorithm

### What is Kosaraju’s Algorithm?

Kosaraju’s Algorithm is an efficient way to find **Strongly Connected Components (SCCs)** in a directed graph. An SCC is a subgraph where every vertex is reachable from every other vertex in that subgraph. The algorithm performs two Depth-First Searches (DFS) and runs in **O(V + E)** time, where V is the number of vertices and E is the number of edges.

### Why Use Kosaraju’s Algorithm?

Kosaraju’s algorithm was chosen because of its simplicity and efficiency in finding strongly connected components in directed graphs. By identifying SCCs, we can compress the graph and treat each component as a single node in a new, smaller graph. This makes it easier to determine the minimum number of additional routes required to connect the entire system.

### Steps Involved in Kosaraju’s Algorithm:

1. **First DFS (Forward Pass)**:
   - Perform a DFS traversal of the graph and push vertices onto a stack based on their finish time (i.e., when all their adjacent nodes are visited).
2. **Transpose the Graph**:

   - Reverse the direction of all edges in the graph. This creates a new graph where all the edges are reversed.

3. **Second DFS (On Transposed Graph)**:

   - Perform DFS on the transposed graph in the order of vertices as stored in the stack from the first DFS.
   - Each DFS call on the transposed graph identifies a strongly connected component.

4. **Compress the Graph**:

   - Once the SCCs are identified, we treat each SCC as a single "super node" and create a new, smaller graph where the nodes represent SCCs.

5. **Calculate the Minimum Additional Routes**:
   - In the new compressed graph, we calculate how many SCCs have zero in-degrees, which indicates that no flight enters them from another SCC.
   - The number of such nodes (SCCs with zero in-degree) represents the minimum number of additional routes needed to connect all airports from the starting point.


**NOTE: Please find an image of the test results in the root directory of the project**




