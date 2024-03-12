import tkinter as tk
#8 Recursive method with return(backtracking)
def show_solution_in_window(board):
    """Displays the placement of queens on the board in a separate window."""
    N = len(board)

    # Create a window
    window = tk.Tk()
    window.title("Queens Placement")

    # Create a canvas for displaying the board
    canvas = tk.Canvas(window, width=N*50, height=N*50, bg='white')
    canvas.pack()

    # Draw the board
    for i in range(N):
        for j in range(N):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill=color)
            if board[i][j] == 1:
                canvas.create_text(j*50 + 25, i*50 + 25, text='♕', font=('Arial', 24))

    window.mainloop()

def solve_queens(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_queens(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_queens(board, 0, N):
        print("Solution not found.")
    else:
        print("Solution found:")
        print_solution(board)
        show_solution_in_window(board)

if __name__ == "__main__":
    N = 16 # Board size
    n_queens(N)
