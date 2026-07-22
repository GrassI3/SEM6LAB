import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(state):
    d = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            d += 1
    return d

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    result = []

    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            s = list(state)
            nz = nr * 3 + nc
            s[z], s[nz] = s[nz], s[z]
            result.append(tuple(s))
    return result

def best_first(start):
    pq = [(heuristic(start), start)]
    visited = set()
    parent = {start: None}

    while pq:
        _, state = heapq.heappop(pq)

        if state == GOAL:
            path = []
            while state:
                path.append(state)
                state = parent[state]
            return path[::-1]

        if state in visited:
            continue
        visited.add(state)

        for nxt in neighbors(state):
            if nxt not in visited:
                parent[nxt] = state
                heapq.heappush(pq, (heuristic(nxt), nxt))

    return []

def print_board(state):
    for i in range(0, 9, 3):
        print(*["_" if x == 0 else x for x in state[i:i+3]])
    print()

start = tuple(map(int, input("Enter 9 numbers: ").split()))

path = best_first(start)

if path:
    print("Solution Found\n")
    for i, state in enumerate(path):
        print("Step", i)
        print_board(state)
else:
    print("No solution")