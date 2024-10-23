def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    visited.add(node)  # Mark the current node as visited
    print(node)  # Process the current node

    for neighbor in graph[node]:  # Visit all the neighbors
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Recursive:")
dfs_recursive(graph, 'A')
