def hill_climbing(graph, start, h):
    current = start
    path = [current]
    
    while True:
        next_node = None
        for node in graph.get(current, []):
            if h[node] < h[current]:
                next_node = node        #if next_node is None or h[node] < h[next_node]:
                break                       #next_node = node
        if not next_node:
            break
        current = next_node
        path.append(current)
    return path


graph = {}
h = {}
while True:
    node = input("Enter node (or 'done' to finish): ").strip()
    if node.lower() == "done":
        break
    graph[node] = input(f"Enter neighbors for {node}: ").split()
print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"Heuristic value for {node}: "))
start = input("\nEnter start node: ").strip()
result = hill_climbing(graph, start, h)

print(" -> ".join(result))