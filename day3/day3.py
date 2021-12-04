from typing import List


def mcv(s: List[str]) -> int:
    return 1 if sum([int(c) for c in s]) / len(s) >= 0.5 else 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
    s = input.splitlines()

    # Part 1
    v0 = int("".join([str(mcv([c[i] for c in s])) for i in range(len(s[0]))]), 2)
    v1 = int("".join([str(1 - mcv([c[i] for c in s])) for i in range(len(s[0]))]), 2)
    print(v0 * v1)

    # Part 2
    s0 = s.copy()
    for i in range(len(s[0])):
        s0 = [c for c in s0 if c[i] == str(mcv([d[i] for d in s0]))]
        if len(s0) == 1:
            break
    s1 = s.copy()
    for i in range(len(s[0])):
        s1 = [c for c in s1 if c[i] != str(mcv([d[i] for d in s1]))]
        if len(s1) == 1:
            break
    print(int(s0[0], 2) * int(s1[0], 2))
