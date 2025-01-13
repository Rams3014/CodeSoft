def initialize_board():
    return [' ' for _ in range(9)]


def display_board(board):
    print(
        f"\n      {board[0]} | {board[1]} | {board[2]}\n"
        "     ---|---|---\n"
        f"      {board[3]} | {board[4]} | {board[5]}\n"
        "     ---|---|---\n"
        f"      {board[6]} | {board[7]} | {board[8]}\n"
    )


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(
        board[pos[0]] == board[pos[1]] == board[pos[2]] == player
        for pos in win_positions
    )


def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']


def minimax(board, is_maximizing):
    if check_winner(board, '⭕'):
        return 1
    if check_winner(board, '❌'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = '⭕'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = '❌'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = '⭕'
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe Game! You are ❌, and the AI 2.0 is ⭕.")
    display_board(board)

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. That spot is already taken! Try again.")
            continue
        print(f"You placed ❌ at position {move + 1}.")
        board[move] = '❌'
        display_board(board)

        if check_winner(board, '❌'):
            print("You win! Congratulations!")
            break
        if ' ' not in board:
            print("It's a tie! Well played!")
            break

        print("AI 2.0 is analyzing its next move...")
        ai_move = find_best_move(board)
        print(f"AI chooses position {ai_move + 1} and places ⭕.")
        board[ai_move] = '⭕'
        display_board(board)

        if check_winner(board, '⭕'):
            print("AI 2.0 wins! Better luck next time!")
            break
        if ' ' not in board:
            print("It's a tie! Well played!")


if __name__ == "__main__":
    play_game()
