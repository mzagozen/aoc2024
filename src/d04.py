import itertools
from collections import defaultdict

def complex_grid(data: list[str]):
    # Place the data in a grid of complex numbers, using a defaultdict to handle out of bounds
    g = defaultdict(str)
    for x, r in enumerate(data):
        for y, c in enumerate(r):
            g[complex(y, x)] = c
    return g


def part1(data):
    dirs = [i + 1j * j for i, j in set(itertools.product([-1, 0, 1], repeat=2)) - {(0, 0)}]
    count = 0
    # defaultdict will create a new entry if the key is not found, so we must store the keys in a list
    for z in list(data.keys()):
        for d in dirs:
            word = [data[z + d * i] for i in range(4)]
            if word == ['X', 'M', 'A', 'S']:
                count += 1

    return count


def part2(data):
    corners = [i + 1j * j for i, j in set(itertools.product([-1, 1], repeat=2))]
    count = 0
    # defaultdict will create a new entry if the key is not found, so we must store the keys in a list
    for z in list(data.keys()):
        if data[z] != 'A':
            continue
        word = [data[z + d] for d in corners]
        # diagonal corners must be a different letter
        if word.count('M') == 2 and word.count('S') == 2 and data[z - 1 + 1j] != data[z + 1 - 1j]:
            count += 1
    return count


def main():
    with open('input/d04.txt') as f:
        data = f.read().splitlines()
    grid = complex_grid(data)
    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()