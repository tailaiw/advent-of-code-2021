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
    mapping = {
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
    # occurance of each stroke: a:8, b:6, c:8, d:7, e:4, f:9, g:7
    result = 0
    for ss in s:
        # map the strokes
        numbers = ss[0]
        count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        for v in numbers:
            for c in v:
                count[c] += 1
        d = {}
        a_and_c = set()
        d_and_g = set()
        for k, v in count.items():
            if v == 4:
                d["e"] = k
            elif v == 6:
                d["b"] = k
            elif v == 9:
                d["f"] = k
            elif v == 8:
                a_and_c.add(k)
            elif v == 7:
                d_and_g.add(k)
        one = set(numbers[[len(n) for n in numbers].index(2)])
        seven = set(numbers[[len(n) for n in numbers].index(3)])
        d["a"] = (seven - one).pop()
        d["c"] = (a_and_c - {d["a"]}).pop()
        six_and_nine_and_zero = [set(n) for n in numbers if len(n) == 6]
        for six_or_nine_or_zero in six_and_nine_and_zero:
            if not six_or_nine_or_zero >= d_and_g:
                d["d"] = (d_and_g - six_or_nine_or_zero).pop()
                d["g"] = (d_and_g - {d["d"]}).pop()
        # convert to number
        output_num = []
        for num in ss[1]:
            for k, v in d.items():
                num = num.replace(v, k.upper())
            num = mapping["".join(sorted(num.lower()))]
            output_num.append(num)
        output_num = int("".join(output_num))
        result += output_num

    print(result)
