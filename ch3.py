import dijkstra
import sidewinder
import pretty

size = 20
dg = dijkstra.DijkstraGrid(size, size)
b = sidewinder.SideWinder(dg)
dg.set_longest_path()
#dg.build_distances(dg.grid[size//2][size//2])
#print(dg)

p = pretty.Pretty(dg)
