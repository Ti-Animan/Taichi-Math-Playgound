"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Count and draw the leaves of an uniform spanning tree
on the 2D square grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random
from itertools import product

import matplotlib.pyplot as plt


def grid_graph(*size):
    """
    Return a grid graph stored in a dict.
    """

    def neighbors(v):
        neighborhood = []
        for i in range(len(size)):
            for dx in [-1, 1]:
                w = list(v)
                w[i] += dx
                if 0 <= w[i] < size[i]:
                    neighborhood.append(tuple(w))
        return neighborhood

    return {v: neighbors(v) for v in product(*map(range, size))}


def main(width, height):
    G = grid_graph(width, height)
    root = random.choice(list(G.keys()))  # choose any vertex as the root.
    tree = {root}  # initially the tree contains only the root.
    parent = {}  # remember the latest step.

    for vertex in G:
        v = vertex
        while v not in tree:
            neighbor = random.choice(G[v])
            parent[v] = neighbor
            v = neighbor
            # can you see how the loops are erased in the above code?

        v = vertex
        while v not in tree:
            tree.add(v)
            v = parent[v]

    fig = plt.figure(figsize=(width // 10, height // 10), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-1, width, -1, height])

    leaves = {node for node in G.keys() if node not in parent.values()}

    # draw the edges.
    for key, item in parent.items():
        a, b = key
        x, y = item
        ax.plot([a, x], [b, y], "k", lw=3)

    # draw the leaves
    for x, y in leaves:
        ax.plot([x], [y], "bo", ms=4)

    n = len(G)
    m = len(leaves)
    print("leaves/allnodes = {}/{} = {}".format(m, n, m / n))
    fig.savefig("ust-leaves-{}-{}.png".format(m, n))


if __name__ == "__main__":
    main(80, 80)
