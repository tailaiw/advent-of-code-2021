import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    ss = np.array(
        [
            [1 if c == ">" else (2 if c == "v" else 0) for c in line]
            for line in input_data.splitlines()
        ]
    )

    step = 0
    while True:
        # east
        ss_pad = np.pad(ss, ((0, 0), (0, 1)), "wrap")
        idx_east = np.argwhere(ss == 1)
        idx_east_movable = idx_east[ss_pad[idx_east[:, 0], idx_east[:, 1] + 1] == 0]
        ss_pad[idx_east_movable[:, 0], idx_east_movable[:, 1]] = 0
        ss_pad[:, -1] = ss_pad[:, 0]
        ss_pad[idx_east_movable[:, 0], idx_east_movable[:, 1] + 1] = 1
        ss = np.roll(ss_pad[:, 1:], 1, axis=1)

        # south
        ss_pad = np.pad(ss, ((0, 1), (0, 0)), "wrap")
        idx_south = np.argwhere(ss == 2)
        idx_south_movable = idx_south[ss_pad[idx_south[:, 0] + 1, idx_south[:, 1]] == 0]
        ss_pad[idx_south_movable[:, 0], idx_south_movable[:, 1]] = 0
        ss_pad[-1, :] = ss_pad[0, :]
        ss_pad[idx_south_movable[:, 0] + 1, idx_south_movable[:, 1]] = 2
        ss = np.roll(ss_pad[1:, :], 1, axis=0)

        step += 1

        if idx_east_movable.shape[0] == 0 and idx_south_movable.shape[0] == 0:
            break

    print(step)
