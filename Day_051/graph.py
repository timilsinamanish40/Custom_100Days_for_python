class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    # Add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            raise ValueError("One or both vertices not found in the graph.")
    
    # Remove an edge between two vertices
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)
    
    # Remove a vertex from the graph
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            # First remove all edges connected to the vertex
            for adjacent_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent_vertex].remove(vertex)
            # Now remove the vertex itself
            del self.adjacency_list[vertex]
    
    # Display the graph
    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# Example usage:
graph = Graph()

# Adding vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Adding edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')

# Display graph
graph.display()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A']
# D: ['B']

# Removing an edge
graph.remove_edge('A', 'B')
graph.display()
# Output:
# A: ['C']
# B: ['D']
# C: ['A']
# D: ['B']

# Removing a vertex
graph.remove_vertex('A')
graph.display()
# Output:
# B: ['D']
# C: []
# D: ['B']
# hi