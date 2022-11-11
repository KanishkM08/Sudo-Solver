import sys
import shutil
import os

import board_prettyprint
import board_solver
import console_user_input

try:
    import inquirer
except ModuleNotFoundError:
    exc_type, exc_value, exc_trace = sys.exc_info()
    missing_module = getattr(exc_value, 'name')

    errtext = f"A required 3rd party module: '{missing_module}' is not installed!\nTo automatically install all requirements, type the following command into your terminal:\npip install -r {os.getcwd()}\\requirements.txt\n\nOr, activate the virtual environment using:\n{os.getcwd()}\\venv\\Scripts\\Activate"
    print(errtext)
    sys.exit(1)


title_file = "assets/ascii_title.txt"
help_file = "assets/ascii_instructions.txt"


def print_title():
    cols, _ = shutil.get_terminal_size()
    with open(title_file, encoding="utf-8") as tf:
        lines = tf.readlines()
        tf.seek(0)

        max_length = max([len(l) for l in lines])
        if cols < max_length:
            os.system(f'mode con: cols={max_length} lines=40')

        print(tf.read())


def print_help():
    with open(help_file, encoding="utf-8") as hf:
        print(hf.read())
    input()


def __loading_animation():
    pass


def run_cli_solving_sequence():
    os.system("cls" if os.name == "nt" else "clear")
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


def construct_prompt(name: str, message: str, choices: list[str]) -> list[inquirer.List]:
    return [inquirer.List(name, message, choices)]


def prompt_user(prompt: list[inquirer.List], name: str) -> str:
    return inquirer.prompt(prompt)[name]


if __name__ == "__main__":
    try:
        print_title()
        print("\n\n\n")

        help_prompt = construct_prompt("help_yn", "Print Help File?", ["Yes", "No"])
        help_yn = prompt_user(prompt=help_prompt, name="help_yn")
        if help_yn == "Yes":
            print_help()

        app_mode_prompt = construct_prompt(
            "app_mode", "Choose application mode:", ["GUI (unavailable)", "CLI"]
        )
        app_mode = prompt_user(prompt=app_mode_prompt, name="app_mode")
        app_mode = "cli"  # TODO Change after implementing GUI

        if app_mode == "cli":
            while True:
                run_cli_solving_sequence()

                solve_another_prompt = construct_prompt(
                    "solve_another", "Solve another board?", ["Yes", "No"]
                )
                solve_another = prompt_user(prompt=solve_another_prompt, name="solve_another").lower()

                if solve_another == "yes":
                    continue

                with open("assets/ascii_thanks.txt", encoding="utf-8") as thxf:
                    print(thxf.read())
                break

    except:
        sys.exit()
        