from itertools import permutations

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    s = [
        (line.split(" | ")[0].split(), line.split(" | ")[1].split())
        for line in input_data.splitlines()
    ]

    # Part 1
    print(len([v for ss in s for v in ss[1] if len(v) in [2, 3, 4, 7]]))

    # Part 2
    m = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }
    perms = [{k: v for k, v in zip("abcdefg", p)} for p in permutations("abcdefg")]
    permed = [
        set(["".join(sorted([p[s] for s in d])) for d in set(m.keys())]) for p in perms
    ]
    output = 0
    for ss in s:
        perm = perms[permed.index(set(["".join(sorted(d)) for d in ss[0]]))]
        inv = {v: k for k, v in perm.items()}
        output += int("".join([m["".join(sorted([inv[s] for s in d]))] for d in ss[1]]))
    print(output)
