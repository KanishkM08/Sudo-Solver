"""
@author Siddharth Vivek
Module to input the board configuration to be solved, from the console.
"""

from copy import copy
import board_prettyprint
from os import system, name as os_name
from config_validity_checker import fullboard_isvalid as board_isvalid

__smaller_title_file = "assets/ascii_smaller_title.txt"


def __cls():
    system('cls' if os_name == 'nt' else 'clear')


def __print_smaller_title():
    with open(__smaller_title_file, encoding='utf-8') as stf:
        print(stf.read())


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
                __print_smaller_title()
                input_num = input(board_str + escape_seq + "<------ [ ] INTEGER FROM 1-9. 0 or No Input for an empty square.\x1B[55D")
                try:
                    int(input_num)
                except ValueError:
                    input_num = '0'

                if input_num == '0': 
                    input_num = ' '
                
                elif 1 <= int(input_num) <= 9:
                    pass

                else:
                    __cls()
                    continue
                
                cp_board_repr = copy(board_repr)
                cp_board_repr[row_idx][col_idx] = int(input_num) if input_num != ' ' else ' '
                __cls()

                # Check the validity of the entered board configuration in its current state
                valid, row_inv, col_inv, box_inv = board_isvalid(cp_board_repr)
                if valid:
                    break
                else:
                    if row_inv: repeat_location = 'row'
                    elif col_inv: repeat_location = 'col'
                    elif box_inv: repeat_location = '3x3 box'

                    print(f"Invalid board configuration! '{input_num}' has been repeated in the same {repeat_location}")
                

            board_repr[row_idx][col_idx] = cp_board_repr[row_idx][col_idx] # int(input_num) if input_num != ' ' else ' '
            __cls()


    print(f"You have entered the following board configuration:\n{board_prettyprint.prettyprint(board_repr, ret=True)}")    

    for row in board_repr:
        for c_idx, item in enumerate(row):
            if item == ' ':
                row[c_idx] = 0

    return board_repr


if __name__ == '__main__':
    test_uin = get_input()
    