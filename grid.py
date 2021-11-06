class Cell:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.links = set()

    def __repr__(self):
        return f"({self.row}, {self.column})"

    # bidirectional link to other
    def link(self, other):
        self.links.add(other)
        other.links.add(self)

    # returns connected neighbouring cells
    def cells(self):
        return self.links

class Grid:
    def __init__(self, rows, columns):
        self.grid = list()
        for r in range(rows):
            self.grid.append(list())
            for c in range(columns):
                self.grid[r].append(Cell(r,c))

        for row in self.grid:
            for cell in row:
                r = cell.row
                c = cell.column

                if r > 0:
                    cell.north = self.grid[r - 1][c]
                if r < len(self.grid) - 1:
                    cell.south= self.grid[r + 1][c]
                if c > 0:
                    cell.west= self.grid[r][c - 1]
                if c < len(row) - 1:
                    cell.east= self.grid[r][c + 1]

    def cells(self):
        l = list()
        for row in self.grid:
            l.extend(row)

        return l

    def dist_weight(self, c):
        return 1

    def get_last_path(self):
        return []

    # returns a string rep of cell count
    def cell_count(self, c):
        return " "

    def __repr__(self):
        header = "+"
        for i in range(len(self.grid[0])):
            header += "---+"
        rep = header + "\n"
        for row in self.grid:
            smid = "|"
            sbot = "+"
            for c in row:
                smid += f" {self.cell_count(c)} "
                if c.east in c.links:
                    smid += " "
                else:
                    smid += "|"

                if c.south in c.links:
                    sbot += "   +"
                else:
                    sbot += "---+"

            rep += smid + "\n" + sbot + "\n"

        return rep


                





