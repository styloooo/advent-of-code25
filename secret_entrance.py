from utils import INPUT_BASE_PATH, read_file
from os.path import join
from combination_lock import CombinationLock

def prepare_input():
    input_path = join(INPUT_BASE_PATH, 'day1.txt')
    return read_file(input_path)

def get_secret_code_part1():
    input_rows = prepare_input()
    secret_code = 0
    lock = CombinationLock()

    for row in input_rows:
        lock.rotate(row)
        if lock.current_value == 0:
            secret_code += 1

    return secret_code

def get_secret_code_part2():
    input_rows = prepare_input()
    secret_code = 0
    lock = CombinationLock()

    for row in input_rows:
        secret_code += lock.rotate(row)

    return secret_code



def main():
    return [get_secret_code_part1(), get_secret_code_part2()]