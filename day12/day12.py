def is_small(node):
    return node.lower() == node


def get_paths(neighbors, current, visits, target, part):
    if current == target:
        return [[]]
    paths = []
    visit = visits.copy()
    visit[current] += 1
    for n in neighbors[current]:
        if (
            (part == 1) and ((is_small(n) and (visit[n] == 0)) or (not is_small(n)))
        ) or (
            (part == 2)
            and (
                (not is_small(n))
                or (is_small(n) and (visit[n] == 0))
                or (
                    is_small(n)
                    and (n not in ["start", "end"])
                    and (max([v for k, v in visit.items() if is_small(k)]) < 2)
                )
            )
        ):
            paths += [[n] + p for p in get_paths(neighbors, n, visit, target, part)]
    return paths


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    ss = [s.split("-") for s in input_data.splitlines()]

    neighbors = dict()
    for s in ss:
        if s[0] in neighbors.keys():
            neighbors[s[0]].append(s[1])
        else:
            neighbors[s[0]] = [s[1]]
        if s[1] in neighbors.keys():
            neighbors[s[1]].append(s[0])
        else:
            neighbors[s[1]] = [s[0]]

    visits = {node: 0 for node in neighbors.keys()}

    print(
        len(get_paths(neighbors, "start", visits, "end", 1)),
        len(get_paths(neighbors, "start", visits, "end", 2)),
    )
