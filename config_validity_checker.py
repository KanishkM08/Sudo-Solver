# __func() = Utility function

def __not_inrow(arr, row):
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before
        if arr[row][i] in st:
            return False
 
        # If not an empty cell, insert value at the current cell in set
        if arr[row][i] != 0:
            st.add(arr[row][i])
     
    return True


# check duplicates in column
def __not_incol(arr, col):
    st = set()
 
    for i in range(0, 9):
 
        # If already encountered before
        if arr[i][col] in st:
            return False
 
        # If not an empty cell, insert value at the current cell in set
        if arr[i][col] != 0:
            st.add(arr[i][col])
     
    return True
 

# check duplicates in 3x3 box
def __not_inbox(arr, startRow, startCol):
 
    st = set()
 
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
 
            # If already encountered before,
            # return false
            if curr in st:
                return False
 
            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != 0:
                st.add(curr)
         
    return True
 

# Get validity of board, and invalidity in ROW, COL, or BOX
def __is_valid(arr, row, col):
    row_inv = not __not_inrow(arr, row)
    col_inv = not __not_incol(arr, col)
    box_inv = not __not_inbox(arr, row - row % 3, col - col % 3)

    return (row_inv, col_inv, box_inv)
 

def currentconfig_isvalid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def fullboard_isvalid(board):
    for row in board:
        for col_idx, item in enumerate(row):
            if item == ' ':
                row[col_idx] = 0
    

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            row_inv, col_inv, box_inv = __is_valid(board, i, j)
            if row_inv or col_inv or box_inv:
                return False, row_inv, col_inv, box_inv # (<is the config VALID?>, <is a row INVALID?>, <is a col INVALID?>, <is a box INVALID?>)
    
    return True, None, None, None


if __name__ == '__main__':
    test_validboard = [
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

    test_invalidboard = [
        [0,0,0,8,0,0,4,2,0],
        [5,0,0,6,7,0,0,0,0],
        [0,5,0,0,0,9,0,0,5],
        [7,4,0,1,0,0,0,0,0],
        [0,0,9,0,3,0,7,0,0],
        [0,0,0,0,0,7,0,4,8],
        [8,0,0,4,0,0,0,0,0],
        [0,0,0,0,9,8,0,0,3],
        [0,9,5,0,0,3,0,0,0]
    ]

    print(fullboard_isvalid(test_validboard))
    print(fullboard_isvalid(test_invalidboard))