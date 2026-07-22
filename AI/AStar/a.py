import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start)]      # (f, g, node)
    parent = {start: None}
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        print(f"Visiting {node}  g={g}  h={h[node]}  f={f}")

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g

        for neigh, cost in graph[node]:
            if neigh not in visited:
                new_g = g + cost
                new_f = new_g + h[neigh]

                if neigh not in parent:
                    parent[neigh] = node

                heapq.heappush(pq, (new_f, new_g, neigh))

    return None, 0


graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("\nNode: ")

    m = int(input(f"Number of neighbours of {node}: "))

    graph[node] = []

    for _ in range(m):
        neigh = input("Neighbour: ")
        cost = int(input("Cost: "))
        graph[node].append((neigh, cost))

print("\nEnter heuristic values")

for node in graph:
    h[node] = int(input(f"h({node}) = "))

start = input("\nStart node: ")
goal = input("Goal node: ")

path, cost = astar(graph, h, start, goal)

print("\nPath :", " -> ".join(path))
print("Cost :", cost)