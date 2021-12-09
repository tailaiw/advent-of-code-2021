import numpy as np

if __name__ == "__main__":
    with open("example.txt", "r") as f:
        input_data = f.read()

    ss = np.array([[int(n) for n in list(s)] for s in input_data.splitlines()])
    wtl = np.hstack(
        [
            10 * np.ones(shape=(ss.shape[0], 1)),
            ss,
            10 * np.ones(shape=(ss.shape[0], 1)),
        ]
    )
    wtl = np.vstack(
        [
            10 * np.ones(shape=(1, wtl.shape[1])),
            wtl,
            10 * np.ones(shape=(1, wtl.shape[1])),
        ]
    )
    idx = (
        (wtl[1:-1, 1:-1] < wtl[1:-1, :-2])
        & (wtl[1:-1, 1:-1] < wtl[1:-1, 2:])
        & (wtl[1:-1, 1:-1] < wtl[:-2, 1:-1])
        & (wtl[1:-1, 1:-1] < wtl[2:, 1:-1])
    )
    print(ss[idx].sum() + idx.sum())

    # Part 2
    output = []
    for i in range(idx.shape[0]):
        for j in range(idx.shape[1]):
            if idx[i, j]:
                wtl = np.zeros(shape=ss.shape)
                wtl[i, j] = 1
                old = wtl.sum()
                while True:
                    for i, j in np.argwhere(wtl):
                        if i != 0 and ss[i - 1, j] != 9:
                            wtl[i - 1, j] = 1
                        if j != 0 and ss[i, j - 1] != 9:
                            wtl[i, j - 1] = 1
                        if i != wtl.shape[0] - 1 and ss[i + 1, j] != 9:
                            wtl[i + 1, j] = 1
                        if j != wtl.shape[1] - 1 and ss[i, j + 1] != 9:
                            wtl[i, j + 1] = 1
                    if wtl.sum() == old:
                        break
                    old = wtl.sum()
                output.append(wtl.sum())
    output = sorted(output)
    print(output[-1] * output[-2] * output[-3])
