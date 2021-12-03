if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    # Part 1
    horiz, depth = 0, 0
    for line in input_data.splitlines():
        dir, step_str = line.split(" ")
        step = int(step_str)
        if dir == "forward":
            horiz += step
        elif dir == "down":
            depth += step
        elif dir == "up":
            depth -= step
    print(horiz * depth)

    # Part 2
    horiz, depth, aim = 0, 0, 0
    for line in input_data.splitlines():
        dir, step_str = line.split(" ")
        step = int(step_str)
        if dir == "forward":
            horiz += step
            depth += aim * step
        elif dir == "down":
            aim += step
        elif dir == "up":
            aim -= step
    print(horiz * depth)
