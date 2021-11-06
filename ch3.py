import grid
import binary
import sidewinder
import pretty
import dijkstra

dg = dijkstra.DijkstraGrid(6, 7)
b = sidewinder.SideWinder(dg)
dg.build_distances(dg.grid[0][0])
dg.path_to(dg.grid[5][0])

print(dg)
#print(d.distances)
#p = pretty.Pretty(g)




