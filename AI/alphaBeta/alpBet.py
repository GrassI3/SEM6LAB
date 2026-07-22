import math

def alphabeta(node, alpha, beta, depth):
    if node not in tree or not tree[node]:
        print("  " * depth + f"{node} = {value[node]}")
        return value[node]

    if depth % 2 == 0:          # MAX
        print("  " * depth + f"MAX {node}")
        best = -math.inf
        for child in tree[node]:
            best = max(best, alphabeta(child, alpha, beta, depth + 1))
            alpha = max(alpha, best)
            if alpha >= beta:
                print("  " * depth + "Beta Pruned")
                break
        return best

    else:                       # MIN
        print("  " * depth + f"MIN {node}")
        best = math.inf
        for child in tree[node]:
            best = min(best, alphabeta(child, alpha, beta, depth + 1))
            beta = min(beta, best)
            if alpha >= beta:
                print("  " * depth + "Alpha Pruned")
                break
        return best

tree = {}
value = {}

n = int(input("Enter number of internal nodes: "))

for i in range(n):
    node = input("\nEnter node name: ")
    children = input(f"Enter children of {node}: ").split()
    tree[node] = children

m = int(input("\nEnter number of leaf nodes: "))

for i in range(m):
    leaf = input("Leaf name: ")
    value[leaf] = int(input(f"Value of {leaf}: "))
    tree[leaf] = []

root = input("\nEnter root node: ")

print("\n----- Alpha Beta Pruning -----\n")
result = alphabeta(root, -math.inf, math.inf, 0)

print("\nOptimal value =", result)