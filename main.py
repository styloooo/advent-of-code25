import secret_entrance
import gift_shop

def day1():
    return secret_entrance.execute()

def day2():
    return gift_shop.execute()


def main():
    day_string_prefix = 'Day'
    
    exercises = [
        (f'{day_string_prefix} 1 (Secret Entrance)', day1()),
        (f'{day_string_prefix} 2 (Gift Shop)', day2()),
    ]

    for exercise in exercises:
        label = exercise[0]
        parts = exercise[1]

        for idx, part_result in enumerate(parts):
            print(f'{label} - Part {idx + 1}: {part_result}')

if __name__ == '__main__':
    main()