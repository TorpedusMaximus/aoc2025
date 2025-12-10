def read_input(path):
    with open(path, 'r') as f:
        raw = f.readlines()
        ranges = True

        fresh_ranges =[]
        products=[]
        for line in raw:
            if line == "\n":
                ranges=False
                continue
            if ranges:
                line = line.strip()
                range_min, range_max = line.split('-')
                fresh_ranges.append((int(range_min),int(range_max)))
            else:
                products.append(int(line.strip()))

    return fresh_ranges, products


def ex1(fresh_ranges, products):
    total_fresh = 0
    for product_id in products:
        for range_min, range_max in fresh_ranges:
            if range_min<= product_id <=range_max:
                total_fresh+=1
                break
    return total_fresh


def ex2(fresh_ranges):
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    if not sorted_ranges:
        return 0

    merged_ranges = []
    curr_start, curr_end = sorted_ranges[0]

    for i in range(1, len(sorted_ranges)):
        next_start, next_end = sorted_ranges[i]

        if next_start <= curr_end:
            curr_end = max(curr_end, next_end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end

    merged_ranges.append((curr_start, curr_end))

    total_fresh = 0
    for start, end in merged_ranges:
        total_fresh += (end - start + 1)

    return total_fresh

if __name__ == "__main__":
    fresh_ranges, products = read_input("input1.txt")
    print(f"Ex1: {ex1(fresh_ranges, products)}")
    print(f"Ex2: {ex2(fresh_ranges)}")
