NUM_VALUES = 100

class CombinationLock:

    def __init__(self):
        self.current_value = 50

    def rotate_right(self, value: int):
        count = 0

        for _ in range(value):
            self.current_value = (self.current_value + 1) % NUM_VALUES
            
            if self.current_value == 0:
                count += 1

        return count

    def rotate_left(self, value: int):
        count = 0

        for _ in range(value):
            self.current_value = (self.current_value - 1) % NUM_VALUES

            if self.current_value == 0:
                count += 1

        return count

    def rotate(self, value_string: str):
        if len(value_string) < 2:
            raise ValueError(f"value_string '{value_string}' cannot have length smaller than 2")

        directions = {'L', 'R'}
        rotate_direction = value_string[0]
        rotate_distance = int(value_string[1:])

        if rotate_direction not in directions:
            raise ValueError(f"rotate direction '{rotate_direction} is not a valid rotation direction")
        elif rotate_direction == 'L':
            return self.rotate_left(rotate_distance)
        else:
            return self.rotate_right(rotate_distance)