def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for n in reversed(graph[node]):
                stack.append(n)
    return visited

graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Node: ")
    graph[node] = input("Neighbours: ").split()
start = input("Start node: ")

print("DFS Traversal:", dfs(graph, start))