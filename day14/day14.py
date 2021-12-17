from collections import Counter

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    s = "+" + input_data.splitlines()[0] + "-"
    rules = {
        line.split(" -> ")[0]: (
            line.split(" -> ")[0][0] + line.split(" -> ")[1],
            line.split(" -> ")[1] + line.split(" -> ")[0][1],
        )
        for line in input_data.splitlines()[2:]
    }

    count = Counter([s[idx : idx + 2] for idx in range(len(s) - 1)])
    for r in range(40):
        new_count = dict()
        for k, v in count.items():
            if k in rules.keys():
                for i in range(2):
                    if rules[k][i] in new_count.keys():
                        new_count[rules[k][i]] += v
                    else:
                        new_count[rules[k][i]] = v
            else:
                new_count[k] = v
        count = new_count

        c_count = dict()
        for k, v in count.items():
            for c in k:
                if c in "+-":
                    continue
                if c in c_count.keys():
                    c_count[c] += v
                else:
                    c_count[c] = v
        c_count = {k: int(v / 2) for k, v in c_count.items()}
        if r == 9 or r == 39:
            print(max(c_count.values()) - min(c_count.values()))
