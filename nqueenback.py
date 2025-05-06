def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >=0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens_backtracking(board, row, n):
    if row == n:
        print_solution(board, n)
        return True  # If you want all solutions, don't return here

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_nqueens_backtracking(board, row + 1, n) or res
            board[row][col] = 0  # Backtrack

    return res

def main():
    n = int(input("Enter the value of n: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_backtracking(board, 0, n):
        print("No solution exists.")

if __name__ == "__main__":
    main()
