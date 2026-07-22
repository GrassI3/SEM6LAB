import heapq

def best_first_search(graph, start, goal, h):
    pq = [(h[start], start)]
    parent = {start: None}
    visited = set()

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current
                heapq.heappush(pq, (h[neighbor], neighbor))

    return None


graph = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = input(f"Enter neighbors of {node}: ").split()
h = {}
print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"Heuristic value for {node}: "))
start = input("Enter starting node: ")
goal = input("Enter goal node: ")
path = best_first_search(graph, start, goal, h)
if path:
    print("\nFinal Path:", " -> ".join(path))
else:
    print("\nNo path found.")