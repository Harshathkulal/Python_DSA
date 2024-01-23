class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start)
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                self.dfs(neighbor, visited)

# Example usage:
# Create a graph and add edges
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

# Perform DFS starting from vertex 1
print("Depth-First Search starting from vertex 1:")
graph.dfs(1)
