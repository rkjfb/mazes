import grid
import binary
import sidewinder
import pretty

g = grid.Grid(15, 15)
# b = binary.BinaryTree(g)
b = sidewinder.SideWinder(g)

print(g)
p = pretty.Pretty(g)




