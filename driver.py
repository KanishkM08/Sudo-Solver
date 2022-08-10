from os import name as os_name
from os import system

import board_prettyprint
import board_solver
import console_user_input

title_file = "assets/ascii_title.txt"
help_file = "assets/ascii_instructions.txt"


def print_title():
    with open(title_file, encoding="utf-8") as tf:
        print(tf.read())


def print_help():
    with open(help_file, encoding="utf-8") as hf:
        print(hf.read())
    input()


def __loading_animation():
    pass


def run_cli_solving_sequence():
    system("cls" if os_name == "nt" else "clear")
    board = console_user_input.get_input()
    solve_state, solved_board = board_solver.solve(board)

    if solve_state:
        print("\n\n\n")
        print("SOLVED! Here's the solution to the entered board:\n\n\n")
        board_prettyprint.prettyprint(solved_board)
        return

    print("\n\n\n")
    print(
        "The entered board cannot be solved! This may be because of a repeated"
        " number or other invalidity in the entered configuration."
    )
    return


if __name__ == "__main__":
    print_title()
    print("\n\n\n")

    help_yn = input("Would you like to run HELP? (y/N) ").lower()
    if not help_yn:
        help_yn = "n"
    if help_yn == "y":
        print_help()

    app_mode = input(
        "Choose the application mode, GUI or CLI. CLI by default (GUI is not "
        "avaliable right now): "
    ).lower()
    app_mode = "cli"  # TODO Change when GUI has been implemented

    if app_mode == "cli":
        while True:
            run_cli_solving_sequence()

            solve_another_yn = input("Solve another board? (Y/n): ").lower()
            if not solve_another_yn:
                pass
            if solve_another_yn not in ["y", "n", ""]:
                solve_another_yn = "y"
            if solve_another_yn == "n":
                with open("assets/ascii_thanks.txt", encoding="utf-8") as thxf:
                    print(thxf.read())
                break
