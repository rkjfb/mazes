import grid

class DijkstraGrid(grid.Grid):

    # builds self.distances, measuring the all the distances from root
    def build_distances(self, root):
        self.distances = dict()
        self.root = root
        self.last_path = None

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

        self.max_cell = max(self.distances, key=self.distances.get)

    def cell_count(self, c):
        if self.last_path != None and not c in self.last_path:
            return " "

        d = self.distances[c]
        base = "0123456789abcdefghijklmnopqrstuvwxyz"
        if d >= len(base):
            raise IndexError(f"{d} is too large for {base}")
        return base[d]

    # return the path to t
    def path_to(self, t):
        path = [t]
        current = t
        while current != self.root:
            for c in current.cells():
                if self.distances[c] < self.distances[current]:
                    current = c
                    path.append(c)
                    break

        self.last_path = path
        return path

    # sets last_path to longest path
    def set_longest_path(self):

        # a longest path starts at the furtherest cell from (0,0)
        self.build_distances(self.grid[0][0])
        origin = self.max_cell

        self.build_distances(origin)
        
        self.path_to(self.max_cell)

    # returns a number between 0 and 1. 0= at origin, 1= at furtherest point
    def dist_weight(self, c):
        max_dist = self.distances[self.max_cell]
        return self.distances[c] / max_dist

    # returns a list of cells on the last path set
    def get_last_path(self):
        return self.last_path




