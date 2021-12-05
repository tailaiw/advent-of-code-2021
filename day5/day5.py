import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    segments = [
        [int(v) for v in line.replace("->", ",").replace(" ", "").split(",")]
        for line in input_data.splitlines()
    ]

    # Part 1
    min_x = min(min([s[0] for s in segments]), min([s[2] for s in segments]),)
    max_x = max(max([s[0] for s in segments]), max([s[2] for s in segments]),)
    min_y = min(min([s[1] for s in segments]), min([s[3] for s in segments]),)
    max_y = max(max([s[1] for s in segments]), max([s[3] for s in segments]),)
    M = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=int)
    for s in segments:
        if (s[0] == s[2]) or (s[1] == s[3]):
            M[
                min(s[1], s[3]) - min_y : max(s[1], s[3]) - min_y + 1,
                min(s[0], s[2]) - min_x : max(s[0], s[2]) - min_x + 1,
            ] += 1

    print((M > 1).sum())

    # Part 2
    for s in segments:
        if (s[0] != s[2]) and (s[1] != s[3]):
            y_range = list(
                range(
                    s[1] - min_y,
                    s[3] - min_y + (1 if (s[1] < s[3]) else -1),
                    1 if (s[1] < s[3]) else -1,
                )
            )
            x_range = list(
                range(
                    s[0] - min_x,
                    s[2] - min_x + (1 if (s[0] < s[2]) else -1),
                    1 if (s[0] < s[2]) else -1,
                )
            )
            M[y_range, x_range] += 1
    print((M > 1).sum())
