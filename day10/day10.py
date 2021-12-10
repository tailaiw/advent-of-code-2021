import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()
    ss = input_data.splitlines()

    error_count = {")": 0, "}": 0, ">": 0, "]": 0}  # for part 1
    scores = []  # for part 2
    for s in ss:
        w = ""
        for c in s:
            # part 1
            if c in ("{", "(", "<", "["):
                w += c
            else:
                if (
                    (w[-1] == "{" and c == "}")
                    or (w[-1] == "(" and c == ")")
                    or (w[-1] == "<" and c == ">")
                    or (w[-1] == "[" and c == "]")
                ):
                    w = w[:-1]
                else:
                    error_count[c] += 1
                    break
        else:
            # part 2
            w = (
                w.replace("(", ")")
                .replace("{", "}")
                .replace("<", ">")
                .replace("[", "]")
            )[::-1]
            score = 0
            for c in w:
                score = score * 5 + (
                    1 if c == ")" else (2 if c == "]" else (3 if c == "}" else 4))
                )
            scores.append(score)

    print(
        error_count[")"] * 3
        + error_count["}"] * 1197
        + error_count[">"] * 25137
        + error_count["]"] * 57
    )  # part 1
    print(int(np.median(scores)))  # part 2
