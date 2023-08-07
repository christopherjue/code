import tkinter as tk
from tkinter import messagebox
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "X"):
        return -10 + depth
    if check_winner(board, "O"):
        return 10 - depth
    if not available_moves(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i, j in available_moves(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in available_moves(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_score = float("-inf")
    best_move = None
    for i, j in available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False, float("-inf"), float("inf"))
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def on_button_click(row, col):
    global player_turn, board

    if player_turn and board[row][col] == " ":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED)
        player_turn = False

        if check_winner(board, "X"):
            messagebox.showinfo("Tic Tac Toe", "You win!")
            root.quit()

        if not available_moves(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()

        ai_turn()

def ai_turn():
    global player_turn, board

    if not player_turn:
        row, col = best_move(board)
        board[row][col] = "O"
        buttons[row][col].config(text="O", state=tk.DISABLED)
        player_turn = True

        if check_winner(board, "O"):
            messagebox.showinfo("Tic Tac Toe", "AI wins!")
            root.quit()

        if not available_moves(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game variables
board = [[" " for _ in range(3)] for _ in range(3)]
player_turn = True  # Player goes first

# Create buttons for the Tic Tac Toe grid
buttons = [[tk.Button(root, text=" ", font=("Helvetica", 20), width=4, height=2,
                      command=lambda i=i, j=j: on_button_click(i, j)) for j in range(3)] for i in range(3)]

# Place buttons on the grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Run the main event loop
root.mainloop()
