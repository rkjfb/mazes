import grid
import binary
import sidewinder
import pretty
import dijkstra

g = dijkstra.DijkstraGrid(3, 4)
b = sidewinder.SideWinder(g)
d = dijkstra.Dijkstra(g, g.grid[0][0])
g.set_distances(d.distances)

print(g)
#print(d.distances)
#p = pretty.Pretty(g)




