from empty_square_finder import find_empty
from config_validity_checker import is_valid

def solve(board):
    empty_sq = find_empty(board)
    if not empty_sq:
        return True, board
    else:
        row, col = empty_sq

    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board)[0]:
                return True, board

            board[row][col] = 0

    return False, None


if __name__ == "__main__":
    test_board = [
        [0,0,0,8,0,0,4,2,0],
        [5,0,0,6,7,0,0,0,0],
        [0,0,0,0,0,9,0,0,5],
        [7,4,0,1,0,0,0,0,0],
        [0,0,9,0,3,0,7,0,0],
        [0,0,0,0,0,7,0,4,8],
        [8,0,0,4,0,0,0,0,0],
        [0,0,0,0,9,8,0,0,3],
        [0,9,5,0,0,3,0,0,0]
    ]

    print(solve(test_board)[1])