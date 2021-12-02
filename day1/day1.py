import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()
    input_data = np.array(input_data.splitlines()).astype(int)

    # Part 1
    print((np.diff(input_data) > 0).sum())

    # Part 2
    print((np.diff(input_data[:-2] + input_data[1:-1] + input_data[2:]) > 0).sum())
