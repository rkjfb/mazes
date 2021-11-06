import dijkstra
import sidewinder

dg = dijkstra.DijkstraGrid(6, 7)
b = sidewinder.SideWinder(dg)
dg.set_longest_path()
print(dg)
