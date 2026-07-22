from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Node: ")
    graph[node] = input("Neighbours: ").split()
start = input("Start node: ")
print("BFS Traversal:", bfs(graph, start))