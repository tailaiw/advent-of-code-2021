from typing import List

import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    lines = input_data.splitlines()
    s = [int(i) for i in lines[0].split(",")]

    boards: List[np.ndarray] = []
    board_raw: List[List[int]] = []
    for line in lines[1:]:
        if line == "":
            if board_raw:
                boards.append(np.array(board_raw))
            board_raw = []
        else:
            board_raw.append([int(i) for i in line.split(" ") if i])
    else:
        boards.append(np.array(board_raw))

    # Part 1
    for i in range(5, len(s)):
        sub = s[: (i + 1)]
        for board in boards:
            if (
                np.isin(board, sub).all(axis=0).any()
                or np.isin(board, sub).all(axis=1).any()
            ):
                print(sum(list(set(board.flatten().tolist()) - set(sub))) * sub[-1])
                break
        else:
            continue
        break

    # Part 2
    won = [False for _ in range(len(boards))]
    for i in range(5, len(s)):
        sub = s[: (i + 1)]
        for k, board in enumerate(boards):
            if won[k]:
                continue
            if (
                np.isin(board, sub).all(axis=0).any()
                or np.isin(board, sub).all(axis=1).any()
            ):
                won[k] = True
                if all(won):
                    print(sum(list(set(board.flatten().tolist()) - set(sub))) * sub[-1])
                    break
        else:
            continue
        break
