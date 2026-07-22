from collections import deque

def is_valid_state(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if (m > 0 and m < c) or ((3 - m) > 0 and (3 - m) < (3 - c)):
        return False
    return True

def solve_missionaries_and_cannibals():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (m, c, boat), path = queue.popleft()
        if (m, c, boat) == goal:
            print("--- OPTIMAL SOLUTION FOUND ---")
            print("Format: (Missionaries on Left, Cannibals on Left, Boat Position)")
            for i in range(len(path)):
                print(f"{path[i]}")
            print(f"\nTotal steps: {len(path)-1}")
            return
        for dm, dc in moves:
            if boat:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if is_valid_state(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")

solve_missionaries_and_cannibals()