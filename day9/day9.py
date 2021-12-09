import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()
    ss = np.array([[int(n) for n in list(s)] for s in input_data.splitlines()])

    # Part 1
    ssp = np.pad(ss, ((1, 1), (1, 1)), "constant", constant_values=10)
    idx = (
        (ssp[1:-1, 1:-1] < ssp[1:-1, :-2])
        & (ssp[1:-1, 1:-1] < ssp[1:-1, 2:])
        & (ssp[1:-1, 1:-1] < ssp[:-2, 1:-1])
        & (ssp[1:-1, 1:-1] < ssp[2:, 1:-1])
    )
    print(ss[idx].sum() + idx.sum())

    # Part 2
    output = []
    for i, j in np.argwhere(idx):
        ev = np.zeros(shape=ss.shape)
        ev[i, j] = 1
        area = 0
        while ev.sum() != area:
            area = ev.sum()
            evp = np.pad(ev, ((1, 1), (1, 1)), "constant", constant_values=0)
            evp += (
                np.roll(evp, 1, axis=0)
                + np.roll(evp, -1, axis=0)
                + np.roll(evp, 1, axis=1)
                + np.roll(evp, -1, axis=1)
            )
            ev = (evp[1:-1, 1:-1] > 0) & (ss != 9)
        output.append(ev.sum())
    output = sorted(output)
    print(output[-1] * output[-2] * output[-3])
