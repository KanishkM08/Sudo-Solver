from turtle import right
import board_prettyprint
from os import system, name as os_name

board_representation = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

for row_idx, row in enumerate(board_representation):
    for col_idx, itm in enumerate(row):
        board_representation[row_idx][col_idx] = '_'
        board_str = board_prettyprint.prettyprint(board_representation, ret=True)
        
        # calculate number of lines to move the cursor UP
        up_num = 0
        if 0 <= row_idx < 3:
            up_num = (len(board_representation) - row_idx) + 2 # skip both horizontal lines
        elif 3 <= row_idx < 6:
            up_num = (len(board_representation) - row_idx) + 1 # skip only the second horizontal line 
        elif row_idx >= 6:
            up_num = len(board_representation) - row_idx # no horizontal lines to skip
        
        escape_code = f"\x1B[{up_num}A\x1B[25C" # escape seq to move cursor UP by up_num lines 

        input_num = input(board_str + escape_code + "<------ [ ]\x1B[2D")

        board_representation[row_idx][col_idx] = int(input_num) 
        system('cls' if os_name == 'nt' else 'clear')

