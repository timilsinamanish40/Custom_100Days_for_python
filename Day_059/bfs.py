
from collections import deque

# Function to perform BFS
def bfs(graph, start_node):
    # Keep track of visited nodes
    visited = set()
    # Use a queue to explore the graph level by level
    queue = deque([start_node])
    
    # Continue until there are no nodes left to explore
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        
        # If the node has not been visited yet
        if node not in visited:
            print(node)  # Process the current node
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS starting from node 'A'
bfs(graph, 'A')
