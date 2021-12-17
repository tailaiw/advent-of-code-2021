import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    idx_dots = np.array(
        [
            tuple([int(xy) for xy in line.split(",")])
            for line in input_data.splitlines()
            if line and (not line.startswith("fold along"))
        ]
    )
    folds = [
        (line[11:].split("=")[0], int(line.split("=")[1]))
        for line in input_data.splitlines()
        if line and line.startswith("fold along")
    ]

    paper = np.zeros((idx_dots[:, 1].max() + 1, idx_dots[:, 0].max() + 1))
    paper[idx_dots[:, 1], idx_dots[:, 0]] = 1

    for i, fold in enumerate(folds):
        if fold[0] == "x":
            diff_fold_len = fold[1] - (paper.shape[1] - 1 - fold[1])
            if diff_fold_len >= 0:
                paper = (
                    paper[:, : fold[1]]
                    + np.pad(
                        paper[:, -1 : fold[1] : -1],
                        ((0, 0), (diff_fold_len, 0)),
                        "constant",
                        constant_values=0,
                    )
                ) > 0
            else:
                paper = (
                    paper[:, -1 : fold[1] : -1]
                    + np.pad(
                        paper[:, : fold[1]],
                        ((0, 0), (-diff_fold_len, 0)),
                        "constant",
                        constant_values=0,
                    )
                ) > 0
        else:
            diff_fold_len = fold[1] - (paper.shape[0] - 1 - fold[1])
            if diff_fold_len >= 0:
                paper = (
                    paper[: fold[1], :]
                    + np.pad(
                        paper[-1 : fold[1] : -1, :],
                        ((diff_fold_len, 0), (0, 0)),
                        "constant",
                        constant_values=0,
                    )
                ) > 0
            else:
                paper = (
                    paper[-1 : fold[1] : -1, :]
                    + np.pad(
                        paper[: fold[1], :],
                        ((-diff_fold_len, 0), (0, 0)),
                        "constant",
                        constant_values=0,
                    )
                ) > 0
        # Part 1
        if i == 0:
            print(paper.sum())
    # Part 2
    plt.imshow(paper)
    plt.show()
