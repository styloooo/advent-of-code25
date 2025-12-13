from os import path
from collections import Counter
from utils import read_file, INPUT_BASE_PATH

def prepare_input() -> list[str]:
    input_path = path.join(INPUT_BASE_PATH, 'day2.txt')
    id_ranges = [id_range.replace('\n', '') for id_range in read_file(input_path)[0].split(',')]
    return id_ranges

def is_id_repeated_sequence(id_to_check: int) -> bool:
    id_to_check = str(id_to_check)

    if len(id_to_check) % 2 != 0:
        return False

    lhs = id_to_check[:len(id_to_check) // 2]

    is_repeated = True if lhs == id_to_check[len(id_to_check) // 2:] else False
    if is_repeated:
        print(f'is_repeated = {is_repeated} for id_to_check = {id_to_check} with lhs = {lhs}')
    return is_repeated


def get_invalid_ids_sum() -> int:
    id_ranges = prepare_input()
    
    invalid_ids = []
    for id_range in id_ranges:
        start_end_list = id_range.split('-')
        start, end = int(start_end_list[0]), int(start_end_list[1])
        for id_value in range(start, end + 1):  # inclusive
            if is_id_repeated_sequence(id_value):
                invalid_ids.append(id_value)

    return sum(invalid_ids)
    

def execute() -> list[int]:
    return [get_invalid_ids_sum(),]