from collections import deque

def water_jug_bfs():
    cap1 = int(input("Enter capacity of Jug 1: "))
    cap2 = int(input("Enter capacity of Jug 2: "))
    goal = int(input("Enter target amount: "))
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    
    goal_states = set()
    solution = 0

    while queue:
        (x, y), path = queue.popleft()
        if x == goal or y == goal:
            if (x, y) not in goal_states:
                goal_states.add((x, y))
                print(f"\n--- Solution {solution} ---")
                print("Format: (Jug1, Jug2)")
                for i in range(len(path)):
                    print(f"Step {i+1}:{path[i]}")
                solution += 1
            continue

        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x)),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    if solution == 0:
        print("No solution found.")
        
water_jug_bfs()