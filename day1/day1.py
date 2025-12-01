def read_input(path):
    with open(path, 'r') as f:
        return [(line[0], int(line[1:])) for line in f]


def ex1(data):
    position = 50
    password = 0

    for rotation, steps in data:
        if rotation == 'L':
            position -= steps
        else:
            position += steps
        position %= 100

        if position == 0:
            password += 1

    return password


def ex2(data):
    position = 50
    password = 0

    for rotation, steps in data:
        prev_position = position

        if rotation == 'L':
            position -= steps
            password += (prev_position - 1) // 100 - (position - 1) // 100
        else:
            position += steps
            password += position // 100 - prev_position // 100

    return password

if __name__=="__main__":
    data = read_input("day1/input1.txt")
    print(f"Ex1: {ex1(data)}")
    print(f"Ex2: {ex2(data)}")
