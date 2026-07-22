N = 4
cols = list(range(N))

def safe(k):
    for i in range(k):
        if abs(cols[i] - cols[k]) == abs(i - k):
            return False
    return True

def solve(k):
    if k == N:
        return True
    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]
        if safe(k) and solve(k + 1):
            return True
        cols[k], cols[i] = cols[i], cols[k]
    return False

if solve(0):
    for r in range(N):
        for c in range(N):
            if cols[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")