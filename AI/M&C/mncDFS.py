def is_valid_state(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if (m > 0 and m < c) or ((3 - m) > 0 and (3 - m) < (3 - c)):
        return False
    return True

def solve_missionaries_and_cannibals_dfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    stack = [(start, [start], [])]
    visited = {start}

    while stack:
        (m, c, boat), path, actions = stack.pop()
        if (m, c, boat) == goal:
            print("--- SOLUTION FOUND (DFS) ---")
            print("Format: (Missionaries on Left, Cannibals on Left, Boat Position)")
            print(f"Start : ({path[0][0]}, {path[0][1]}, {'L' if path[0][2] else 'R'})")
            
            for i, action in enumerate(actions):
                lm, lc, b = path[i + 1]
                print(f"Step {i+1}: {action.ljust(22)} -> State: ({lm}, {lc}, {'L' if b else 'R'})")
            print(f"\nTotal steps: {len(actions)}")
            return

        for dm, dc in moves:
            if boat:
                new_state = (m - dm, c - dc, 0)
                action = f"Move {dm}M, {dc}C Right"
            else:
                new_state = (m + dm, c + dc, 1)
                action = f"Move {dm}M, {dc}C Left"

            if is_valid_state(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [new_state], actions + [action]))

    print("No solution found.")
solve_missionaries_and_cannibals_dfs()