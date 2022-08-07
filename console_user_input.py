"""
@author Siddharth Vivek
Module to input the board configuration to be solved, from the console.
"""

import board_prettyprint
from os import system, name as os_name


def cls():
    system('cls' if os_name == 'nt' else 'clear')


# Calculate the number of lines to move the cursor UP by
def calc_up_num(row_idx: int, board_repr: list[list[str]]):
    """
    @returns str: Escape Sequence to move the cursor UP by some number of lines
    """

    up_num = 0
    if 0 <= row_idx < 3:
        up_num = (len(board_repr) - row_idx) + 2 # skip both horizontal lines
    elif 3 <= row_idx < 6:
        up_num = (len(board_repr) - row_idx) + 1 # skip only the second horizontal line 
    elif row_idx >= 6:
        up_num = len(board_repr) - row_idx # no horizontal lines to skip
    escape_seq = f"\x1B[{up_num}A\x1B[25C" # escape seq to move cursor UP by up_num lines

    return escape_seq


def get_input() -> list[list[int]]:
    """
    @returns list[list[int]]: Board configuration to be solved, as per user input
    """

    board_repr = [
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

    for row_idx, row in enumerate(board_repr):
        for col_idx, _ in enumerate(row):
            board_repr[row_idx][col_idx] = '_'
            board_str = board_prettyprint.prettyprint(board_repr, ret=True)
            
            escape_seq = calc_up_num(row_idx, board_repr)
            
            while True:
                try:
                    input_num = int(input(board_str + escape_seq + "<------ [ ] INTEGER FROM 1-9. 0 or No Input for an empty square.\x1B[55D"))
                except ValueError:
                    input_num = 0
                
                if 0 <= input_num <= 9:
                    break

                cls()
                print("Please enter a valid value for the board. Integer from 1 - 9, 0 or no input for an empty square.\n") 

            board_repr[row_idx][col_idx] = int(input_num) 
            cls()

    print(f"You have entered the following board configuration:\n{board_prettyprint.prettyprint(board_repr, ret=True)}")
    return board_repr


if __name__ == '__main__':
    test_uin = get_input()
    