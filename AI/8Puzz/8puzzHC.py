GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(state):
    d = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            d += 1          # Misplaced tiles heuristic
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

def hill_climbing(start):
    current = start
    path = [current]

    while True:
        next_node = None

        for node in neighbors(current):
            if heuristic(node) < heuristic(current):
                if next_node is None or heuristic(node) < heuristic(next_node):
                    next_node = node

        if next_node is None:
            break

        current = next_node
        path.append(current)

    return path, current == GOAL

def print_board(state):
    for i in range(0, 9, 3):
        for x in state[i:i+3]:
            print("_" if x == 0 else x, end=" ")
        print()
    print()

start = tuple(map(int, input("Enter 9 numbers: ").split()))

path, solved = hill_climbing(start)

for i, state in enumerate(path):
    print("Step", i)
    print_board(state)

if solved:
    print("Solution Found")
else:
    print("Stuck at Local Optimum")