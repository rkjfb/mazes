import grid

class Dijkstra:

    # builds self.distances, measuring the all the distances from root in grid
    def build_distances(self, grid, root):
        self.distances = dict()
        d = 0
        frontier = [root]

        while len(frontier) > 0:
            new_frontier = []
            for c in frontier:
                if c in self.distances:
                    continue
                self.distances[c] = d
                new_frontier.extend(c.cells())

            frontier = new_frontier
            d += 1


    def __init__(self, grid, root):
        self.build_distances(grid, root)

class DijkstraGrid(grid.Grid):
    def set_distances(self, d):
        self.distances = d

    def cell_count(self, c):
        d = self.distances[c]
        base = "0123456789abcdefghijklmnopqrstuvwxyz"
        if d >= len(base):
            raise IndexError(f"{d} is too large for {base}")
        return base[d]



