def prettyprint(board: list[list[str]], ret: bool = False):
    ret_str = ''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            ret_str += "- - - - - - - - - - - -  \n"

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                ret_str += " | "

            if j == 8:
                ret_str += f"{str(board[i][j])}\n"
            else:
                ret_str += str(board[i][j]) + " "

    if ret:
        return ret_str

    print(ret_str)


if __name__ == "__main__":
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

    prettyprint(board_representation)