def read_input(path):
    with open(path, 'r') as f:
        data = f.readlines()

    return data


def get_max_joltage(bank, num_batteries):
    first_max = (-1, 0)
    for index, battery in enumerate(bank[:-(num_batteries - 1)]):
        if int(battery) == 9:
            first_max = (index, int(battery))
            break
        if int(battery) > first_max[1]:
            first_max = (index, int(battery))

    maxes = [first_max]

    for i in range(num_batteries - 2, -1, -1):
        next_max = maxes[-1]
        even_next_max = (-1, 0)
        for index, battery in enumerate(bank[next_max[0] + 1:-i] if i > 0 else bank[next_max[0] + 1:]):
            if int(battery) == 9:
                maxes.append((index + next_max[0] + 1, int(battery)))
                break
            if int(battery) > even_next_max[1]:
                even_next_max = (index + next_max[0] + 1, int(battery))
        else:
            maxes.append(even_next_max)

    return int("".join([str(max_value) for _, max_value in maxes]))


def ex(data, num_batteries):
    total_joltage = 0
    for bank in data:
        total_joltage += get_max_joltage(bank.strip(), num_batteries)

    return total_joltage


if __name__ == "__main__":
    data = read_input("input1.txt")
    print(f"Ex1: {ex(data, 2)}")
    print(f"Ex2: {ex(data, 12)}")
