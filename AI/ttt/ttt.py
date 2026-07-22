WIN = [ [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] ]

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
    print()

def winner(board):
    for a, b, c in WIN:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def minimax(board, is_max):
    result = winner(board)

    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, False))
                board[i] = " "
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, True))
                board[i] = " "
        return best

def ai_move(board):
    best = 999
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True)
            board[i] = " "

            if score < best:
                best = score
                move = i

    return move

board = [" "] * 9

while winner(board) is None:
    print_board(board)

    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] != " ":
        print("Invalid move")
        continue

    board[pos] = "X"

    if winner(board):
        break

    board[ai_move(board)] = "O"

print_board(board)

result = winner(board)

if result == "X":
    print("You Win")
elif result == "O":
    print("AI Wins")
else:
    print("Draw")