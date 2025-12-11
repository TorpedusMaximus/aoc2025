from functools import cache


def read_input(path):
    with open(path, 'r') as f:
        raw = f.readlines()

    data = {}
    for row in raw:
        row = row.strip()
        device, outputs = row.split(':')
        data[device] = outputs.strip().split(' ')
    data["out"] = []
    return data


def count_paths(data, path):
    start, end = path

    @cache
    def count_paths_from_node(node):
        if node == end:
            return 1
        total = 0
        for neighbor in data[node]:
            total += count_paths_from_node(neighbor)

        return total

    return count_paths_from_node(start)


def ex1(data):
    return count_paths(data, ('you', 'out'))


def ex2(data):
    paths = [
        ("svr", "fft"),
        ("fft", "dac"),
        ("dac", "out"),

        ("svr", "dac"),
        ("dac", "fft"),
        ("fft", "out"),
    ]
    results = [count_paths(data, path) for path in paths]
    return (results[0] * results[1] * results[2]) + (
            results[3] * results[4] * results[5])


if __name__ == "__main__":
    data = read_input("input1.txt")
    print(f"Ex1: {ex1(data)}")
    print(f"Ex2: {ex2(data)}")
    pass
