from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
# Define an adjacency list representation of a graph
# {node: [list of neighbors]}
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E']
}

# Start BFS from node 'A'
bfs(graph, 'A')
