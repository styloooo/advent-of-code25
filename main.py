from secret_entrance import main as secret_entrance_main

def day1():
    return secret_entrance_main()

def main():
    day_string_prefix = 'Day'
    
    exercises = [
        (f'{day_string_prefix} 1 (Secret Entrance)', day1()),
    ]

    for exercise in exercises:
        label = exercise[0]
        parts = exercise[1]

        for idx, part_result in enumerate(parts):
            print(f'{label} - Part {idx + 1}: {part_result}')

if __name__ == '__main__':
    main()