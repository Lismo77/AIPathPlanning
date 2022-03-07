from queue import PriorityQueue
import PathPlanning

pq = PriorityQueue()

vx1 = PathPlanning.Vertex(1,1)
vx2 = PathPlanning.Vertex(2,2)
vx3 = PathPlanning.Vertex(3,3)

pq.put((vx1.x*vx1.y, vx1))
pq.put((vx2.x*vx2.y, vx2))
pq.put((vx3.x*vx3.y, vx3))

pq.get((vx2.x*vx2.y, vx2))
print(pq.get()[1].str())
print(pq.get()[1].str())

'''
PathPlanning.Grid.generate_grid(4,3)
grid = PathPlanning.Grid()
grid.populate_grid('gridtext.txt')
PathPlanning.Vertex.goal_vertex = grid.goal

path = grid.a_star()
if path is not None :
    for i in path :
        print(i.str())
'''

