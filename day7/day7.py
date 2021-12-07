def g(n: int) -> int:
    return int((1 + n) * n / 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    s = [int(i) for i in input_data.split(",")]

    # Part 1
    min_dist = float("inf")
    for i in range(min(s), max(s) + 1):
        dist = sum([abs(v - i) for v in s])
        if dist < min_dist:
            min_dist = dist
    print(min_dist)

    # Part 2
    min_dist = float("inf")
    for i in range(min(s), max(s) + 1):
        dist = sum([g(abs(v - i)) for v in s])
        if dist < min_dist:
            min_dist = dist
    print(min_dist)
