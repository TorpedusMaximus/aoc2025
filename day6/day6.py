import numpy as np


def read_input_ex1(path):
    with open(path, 'r') as f:
        raw = f.readlines()

        data = []
        for row in raw:
            data.append(row.split())

        values = np.array(data[:-1]).astype(int)
        operations = np.array(data[-1])

    return values, operations


def read_input_ex2(path):
    with open(path, 'r') as f:
        raw = f.readlines()
        data = []
        max_row_length = 0
        for row in raw:
            row_split = [
                character
                for character in row
                if character != '\n'
            ]
            if len(row_split) > max_row_length:
                max_row_length = len(row_split)

            data.append(row_split)

        data_cleaned = []
        for row in data:
            difference = max_row_length - len(row)
            data_cleaned.append(row + ['' for _ in range(difference)])

        data = np.array(data_cleaned)

    operations = np.array(data[-1])
    operations = operations[operations != ' ']
    operations = operations[operations != '']
    values = np.array(data[:-1])

    results = []
    for column_id in range(values.shape[1]):
        current_value = ""
        for value in values[:, column_id]:
            if value != ' ':
                current_value += value
        results.append(current_value)

    split = []
    current_group = []
    for value in results:
        if value == '':
            split.append(current_group)
            current_group = []
        else:
            current_group.append(int(value))
    split.append(current_group)

    return split, operations


def ex1(values, operations):
    mask = operations == '+'

    additions = values[:, mask]
    multiplications = values[:, ~mask]

    total = additions.sum()

    multiplications = multiplications.prod(axis=0)
    total += multiplications.sum()

    return total


def ex2(values, operations):
    total = 0
    for group, operation in zip(values, operations):
        if operation == "+":
            total += sum(group)
        else:
            total += np.prod(group)

    return total


if __name__ == "__main__":
    values, operations = read_input_ex1("input1.txt")
    print(f"Ex1: {ex1(values, operations)}")
    values, operations = read_input_ex2("input1.txt")
    print(f"Ex2: {ex2(values, operations)}")
