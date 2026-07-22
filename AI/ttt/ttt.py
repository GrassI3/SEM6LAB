WIN = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def winner(b):
    for x,y,z in WIN:
        if b[x] == b[y] == b[z] != " ":
            return b[x]
    if " " not in b:
        return "D"
    return None

def minimax(b, turn):
    w = winner(b)
    if w == "X": return 1
    if w == "O": return -1
    if w == "D": return 0

    best = -999 if turn == "X" else 999
    for i in range(9):
        if b[i] == " ":
            b[i] = turn
            if turn == "X": best = max(best, minimax(b, "O"))
            else: best = min(best, minimax(b, "X"))
            b[i] = " "
    return best

def ai_move(b):
    best = 999
    move = 0
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(b, "X")
            b[i] = " "
            if score < best:
                best = score
                move = i
    return move

board = [" "] * 9

while winner(board) is None:
    for i in range(0,9,3):
        print(" | ".join(board[i:i+3]))
    board[int(input("Move (1-9): ")) - 1] = "X"
    if winner(board):
        break
    board[ai_move(board)] = "O"

for i in range(0,9,3):
    print(" | ".join(board[i:i+3]))
print("Winner:", winner(board))