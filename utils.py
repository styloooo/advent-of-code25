from os import path, getcwd

INPUT_BASE_PATH = path.join(getcwd(), 'input')

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [row for row in f]