import numpy as np

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()

    energy = np.array([[int(n) for n in s] for s in input_data.splitlines()])

    total_flash = 0
    for step in range(1000):
        flashed = np.zeros(energy.shape)
        energy += 1
        while True:
            flash = np.pad(
                (energy > 9) & (flashed == 0),
                ((1, 1), (1, 1)),
                "constant",
                constant_values=0,
            ).astype(int)
            flashed[flash[1:-1, 1:-1] == 1] = 1
            energy[flash[1:-1, 1:-1] == 1] = 0
            energized = (
                np.roll(flash, 1, axis=0)
                + np.roll(flash, -1, axis=0)
                + np.roll(flash, 1, axis=1)
                + np.roll(flash, -1, axis=1)
                + np.roll(np.roll(flash, 1, axis=0), 1, axis=1)
                + np.roll(np.roll(flash, -1, axis=0), 1, axis=1)
                + np.roll(np.roll(flash, 1, axis=0), -1, axis=1)
                + np.roll(np.roll(flash, -1, axis=0), -1, axis=1)
            )[1:-1, 1:-1]
            if not np.any(energized):
                break
            else:
                energy += energized
        energy[flashed == 1] = 0
        if energy.sum() == 0:  # Part 2
            print(f"Part 2: {step + 1}")
            break
        total_flash += np.sum(flashed.astype(int))
        if step + 1 == 100:  # Part 1
            print(f"Part 1: {total_flash}")
