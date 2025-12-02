def read_input(path):
    with open(path, 'r') as f:
        raw = f.readline()
        raw = raw.split(',')
        data = []
        for row in raw:
            r1, r2 = row.split('-')
            data.append((int(r1), int(r2)))
    return data


def valid_ex1(product_id):
    first_half = str(product_id)[:int(len(str(product_id)) / 2)]
    second_half = str(product_id)[int(len(str(product_id)) / 2):]

    if first_half == second_half:
        return product_id
    return 0


def valid_ex2(product_id):
    s = str(product_id)
    if s in (s + s)[1:-1]:
        return product_id
    return 0


def ex(data, valid):
    invalid = 0
    for r1, r2 in data:
        for product_id in range(r1, r2 + 1):
            invalid += valid(product_id)
    return invalid

if __name__=="__main__":
    data = read_input("input1.txt")
    print(f"Ex1: {ex(data, valid_ex1)}")
    print(f"Ex2: {ex(data, valid_ex2)}")
