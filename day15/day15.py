import numpy as np


def expand(w):
    new_w = w + 1
    new_w[new_w > 9] = 1
    return new_w


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    w = np.array([[int(c) for c in line] for line in input_data.splitlines()])

    # comment this section for part 1
    w = np.hstack(
        [
            w,
            expand(w),
            expand(expand(w)),
            expand(expand(expand(w))),
            expand(expand(expand(expand(w)))),
        ]
    )
    w = np.vstack(
        [
            w,
            expand(w),
            expand(expand(w)),
            expand(expand(expand(w))),
            expand(expand(expand(expand(w)))),
        ]
    )

    dist = np.ones(w.shape) * np.inf
    dist[0, 0] = w[0, 0]
    visited = np.ones(w.shape)
    while True:
        idx = np.unravel_index(np.argmin(dist * visited, axis=None), dist.shape)
        print(idx)
        visited[idx] = np.inf
        if idx[0] > 0 and visited[idx[0] - 1, idx[1]] == 1:
            dist[idx[0] - 1, idx[1]] = min(
                dist[idx[0] - 1, idx[1]], dist[idx] + w[idx[0] - 1, idx[1]]
            )
        if idx[0] < w.shape[0] - 1 and visited[idx[0] + 1, idx[1]] == 1:
            dist[idx[0] + 1, idx[1]] = min(
                dist[idx[0] + 1, idx[1]], dist[idx] + w[idx[0] + 1, idx[1]]
            )
        if idx[1] > 0 and visited[idx[0], idx[1] - 1] == 1:
            dist[idx[0], idx[1] - 1] = min(
                dist[idx[0], idx[1] - 1], dist[idx] + w[idx[0], idx[1] - 1]
            )
        if idx[1] < w.shape[1] - 1 and visited[idx[0], idx[1] + 1] == 1:
            dist[idx[0], idx[1] + 1] = min(
                dist[idx[0], idx[1] + 1], dist[idx] + w[idx[0], idx[1] + 1]
            )
        if idx == (w.shape[0] - 1, w.shape[1] - 1):
            print(dist[idx] - w[0, 0])
            break
