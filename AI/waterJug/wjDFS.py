def water_jug_dfs():
    cap1 = int(input("Enter capacity of Jug 1: "))
    cap2 = int(input("Enter capacity of Jug 2: "))
    goal = int(input("Enter target amount: "))

    start = (0, 0)
    stack = [(start, [start])]
    visited = {start}
    goal_states = set()
    solution = 1

    while stack:
        (x, y), path = stack.pop()

        if x == goal or y == goal:
            if (x, y) not in goal_states:
                goal_states.add((x, y))

                print(f"\n--- Solution {solution} ---")
                print("Format: (Jug1, Jug2)")
                print(f"Start : {path[0]}")

                for i in range(len(path)-1):
                    print(f"Step {i+1}: {path[i+1]}")

                print(f"Total steps: {len(path) - 1}")
                solution += 1
            continue

        next_states = [
            ((cap1, y)),
            ((x, cap2)),
            ((0, y)),
            ((x, 0)),
            ((x - min(x, cap2 - y), y + min(x, cap2 - y))),
            ((x + min(y, cap1 - x), y - min(y, cap1 - x)))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                stack.append((state, path + [state]))

    if solution == 1:
        print("No solution found.")
water_jug_dfs()