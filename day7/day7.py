def g(n: int) -> int:
    return int((1 + n) * n / 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    s = [int(i) for i in input_data.split(",")]

    # Part 1
    print(min([sum([abs(v - i) for v in s]) for i in range(0, max(s) + 1)]))

    # Part 2
    print(min([sum([g(abs(v - i)) for v in s]) for i in range(0, max(s) + 1)]))
