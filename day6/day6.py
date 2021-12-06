if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    count = {k: sum([int(v) == k for v in input_data.split(",")]) for k in range(9)}

    for _ in range(256):
        count = {
            (k - 1) if (k - 1 >= 0) else 8: v if (k - 1 != 6) else (v + count[0])
            for k, v in count.items()
        }
    print(sum(count.values()))
