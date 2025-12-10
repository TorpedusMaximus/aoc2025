import numpy as np


def read_input(path):
    with open(path, 'r') as f:
        raw = f.readlines()
        data = []
        for row in raw:
            row = row.strip()
            t = []
            for cell in row:
                if cell == '.':
                    t.append(0)
                else:
                    t.append(1)
            data.append(t)

    return np.array(data)


def ex(data):
    padded = np.pad(data, 1, constant_values=0)
    moved = []
    while True:
        to_move = []
        for x, row in enumerate(padded):
            for y, cell in enumerate(row):
                if cell == 1:
                    if padded[x - 1:x + 2, y - 1:y + 2].sum() < 5:
                        to_move.append((x, y))
        if len(to_move) == 0:
            break
        moved.append(len(to_move))
        for x, y in to_move:
            padded[x, y] = 0

    print(padded)

    return moved


if __name__ == "__main__":
    data = read_input("input1.txt")
    moved = ex(data)
    print(f"Ex1: {moved[0]}")
    print(f"Ex2: {sum(moved)}")
