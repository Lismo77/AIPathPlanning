import math
import random
from queue import PriorityQueue

class Vertex :

    goal_vertex = None     # class variable for goal node

    # constructor
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.g = None
        self.pv = None

    # getters and setters for x and y coordinates of vertex
    def get_x(self) :
        return self.x
    def set_x(self, x) :
        self.x = x
    def get_y(self) :
        return self.y
    def set_y(self, y) :
        self.y = y
    def get_g(self) :
        return self.g

    # getters and setters for parent vertex
    def get_pv(self) :
        return self.pv
    def set_pv(self, parent) :
        self.pv = parent
        if self.pv is not None :
            self.g = self.get_distance(self.get_pv()) + self.get_pv().get_g()
        

    # methods for calculating the g, h, and f values 
    def set_g(self, gval) :
        self.g = gval
    def get_h(self) :
        h = math.sqrt(2) * min(abs(self.get_x() - Vertex.goal_vertex.get_x()), abs(self.get_y() - Vertex.goal_vertex.get_y())) + max(abs(self.get_x() - Vertex.goal_vertex.get_x()), abs(self.get_y() - Vertex.goal_vertex.get_y())) - min(abs(self.get_x() - Vertex.goal_vertex.get_x()), abs(self.get_y() - Vertex.goal_vertex.get_y()))      # algorithm from assignment page
        return h
    def get_thetah(self) :
        h = self.get_distance(Vertex.goal_vertex)        # straight line h value
        return h
    def get_f(self) :
        return self.get_g() + self.get_h()
    def get_thetaf(self) :
        return self.get_g() + self.get_thetah()

    # method that calculates distance between two vertices
    def get_distance(self, vert) :
        distance = math.sqrt((abs(self.get_x() - vert.get_x()) ** 2) + (abs(self.get_y() - vert.get_y()) ** 2))
        return distance    

    # vertex to string method
    def str(self) :
        return str(self.x) + ', ' + str(self.y)

# class for individual cell blocks
class Cell :
    
    # cell constructor
    def __init__(self, tl_vertex,  blocked) :
        self.tl_vertex = tl_vertex
        self.blocked = blocked

    # getters and setters
    def get_tl_vertex(self) :
        return self.tl_vertex
    def get_blocked(self) :
        return self.blocked
    def set_blocked(self, blockage) :
        self.blocked = blockage

    # to string method
    def str(self) :
        return self.tl_vertex.str() + ", " + str(self.get_blocked())
 
        
class Grid :

    # grid constructor
    def __init__(self) :
        self.start = None
        self.goal = None
        self.vertex_list = None
        self.cell_list = None
        self.dimensions = [0, 0]

    # getters/setters
    def get_start(self) :
        return self.start
    def set_start(self, start) :
        self.start = start
    def get_goal(self) :
        return self.goal
    def set_goal(self, goal) :
        self.goal = goal

    def find_neighbors(self, current_vert) :        # method finds all valid neighbors (lines commented out updates their parent values to current_vert)
        neighbors = []
        if self.cell_list[current_vert.y - 1][current_vert.x - 1].get_blocked() == 0 :
            #self.vertex_list[current_vert.y - 1][current_vert.x - 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y - 1][current_vert.x - 1])
            #self.vertex_list[current_vert.y - 1][current_vert.x].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y - 1][current_vert.x])
        elif self.cell_list[current_vert.y - 1][current_vert.x].get_blocked() == 0 :
            #self.vertex_list[current_vert.y - 1][current_vert.x].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y - 1][current_vert.x])
        if self.cell_list[current_vert.y - 1][current_vert.x].get_blocked() == 0 :
            #self.vertex_list[current_vert.y][current_vert.x + 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y][current_vert.x + 1])
            #self.vertex_list[current_vert.y - 1][current_vert.x + 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y - 1][current_vert.x + 1])
        elif self.cell_list[current_vert.y][current_vert.x].get_blocked() == 0 :
            #self.vertex_list[current_vert.y][current_vert.x + 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y][current_vert.x + 1])
        if self.cell_list[current_vert.y][current_vert.x].get_blocked() == 0 :
            #self.vertex_list[current_vert.y + 1][current_vert.x + 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y + 1][current_vert.x + 1])
            #self.vertex_list[current_vert.y + 1][current_vert.x].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y + 1][current_vert.x])
        elif self.cell_list[current_vert.y][current_vert.x - 1].get_blocked() == 0 :
            #self.vertex_list[current_vert.y + 1][current_vert.x].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y + 1][current_vert.x])
        if self.cell_list[current_vert.y][current_vert.x - 1].get_blocked() == 0 :
            #self.vertex_list[current_vert.y + 1][current_vert.x - 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y + 1][current_vert.x - 1])
            #self.vertex_list[current_vert.y][current_vert.x - 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y][current_vert.x - 1])
        elif self.cell_list[current_vert.y - 1][current_vert.x - 1].get_blocked() == 0 :
            #self.vertex_list[current_vert.y][current_vert.x - 1].set_pv(current_vert)
            neighbors.append(self.vertex_list[current_vert.y][current_vert.x - 1])
        return neighbors
            
    @staticmethod
    def generate_grid(xdimen, ydimen) :       # generates a text file named 'gridtext.txt' of a grid in the format from assignment page
        vertices = [[None]*(xdimen+3) for _ in range((ydimen+3))]
        cells = [[None]*(xdimen+2) for _ in range((ydimen+2))]

        for i in range(len(vertices)) :     # populates vertex list
            for j in range(len(vertices[0])) :
                vertices[i][j] = Vertex(j, i)

        for i in range(len(cells)) :        # populates cell list
            for j in range(len(cells[0])) :
                if i == 0 or i == ydimen+1 or j == 0 or j == xdimen+1:      # checks if they are a border cell
                    cells[i][j] = Cell(vertices[i][j], 1)
                else : 
                    blocked_prob = random.random()
                    if (blocked_prob <= .1) :
                        cells[i][j] = Cell(vertices[i][j], 1)
                    else :
                        cells[i][j] = Cell(vertices[i][j], 0)
        
        start_vertex = random.choice(random.choice(vertices))       # chooses a random starting vertex and retries if it is out of bounds
        while (start_vertex.get_x() == 0 or start_vertex.get_x() == xdimen+2 or start_vertex.get_y() == 0 or start_vertex.get_y() == ydimen+2) :
            start_vertex = random.choice(random.choice(vertices))
        goal_vertex = random.choice(random.choice(vertices))        # chooses a random goal vertex and retries if it is out of bounds
        while (goal_vertex.get_x() == 0 or goal_vertex.get_x() == xdimen+2 or goal_vertex.get_y() == 0 or goal_vertex.get_y() == ydimen+2) :
            goal_vertex = random.choice(random.choice(vertices))
        with open('gridtext.txt', 'w') as grid_file :               # writes start vertex, goal vertex, and all cells to new txt file
            grid_file.write(start_vertex.str() + '\n')
            grid_file.write(goal_vertex.str() + '\n')
            grid_file.write(str(xdimen) + ', ' + str(ydimen) + '\n')
            for j in range(1, len(cells[0])-1) :
                for i in range(1, len(cells)-1) :
                    grid_file.write(cells[i][j].str() + '\n')
            
    
    def populate_grid(self, grid_name) :     # method that reads in file name and populates grid object
        gridfile = open(grid_name, 'r')
        lines = gridfile.readlines()
        start = lines[0].split(',')
        self.start = Vertex(int(start[0]), int(start[1]))
        goal = lines[1].split(',')
        self.goal = Vertex(int(goal[0]), int(goal[1]))
        dimen = lines[2].split(',')
        self.dimensions = [int((dimen[0])), int(dimen[1])]
        vertices = [[None]*(self.dimensions[0]+3) for _ in range((self.dimensions[1]+3))]
        cells = [[None]*(self.dimensions[0]+2) for _ in range((self.dimensions[1]+2))]

        for i in range(len(vertices)) :     # populates vertex list
            for j in range(len(vertices[0])) :
                vertices[i][j] = Vertex(j, i)

        for i in range(len(cells)) :        # populates cell list
            for j in range(len(cells[0])) :
                cells[i][j] = Cell(vertices[i][j], 1)
                        
        for i in range(3, len(lines)) :
            this_cell = lines[i].split(',')
            blockage = int(this_cell[2])
            if blockage == 0 :
                cells[int(this_cell[1])][int(this_cell[0])].set_blocked(0)
        
        self.vertex_list = vertices
        self.cell_list = cells
    

    def a_star(self) :      # performs A* algorithm and returns a list containing the vertices that make up the shortest path
        Vertex.goal_vertex = self.goal
        self.start.set_g(0)
        self.start.set_pv(self.start)
        fringe = PriorityQueue()
        fringe.put((self.start.get_f(), self.start.get_h(), self.start))
        closed = []
        while not fringe.empty() :
            current = fringe.get()[2]
            if current.get_h() == 0 :
                path = []
                while current is not self.start :
                    path.append(current)
                    current = current.pv
                path.append(self.start)
                path.reverse()
                print('Path found')
                return path
                
            closed.append(current)
            for successor in self.find_neighbors(current) :
                if successor not in closed :
                    if not any(successor in item for item in fringe.queue) :
                        successor.set_g(math.inf)
                        successor.set_pv(None)
                    self.a_updatevx(fringe, current, successor)
        print('No path found')
        return None
    
    def theta_star(self) :      # performs Theta* algorithm and returns a list containing the vertices that make up the shortest path
        Vertex.goal_vertex = self.goal
        self.start.set_g(0)
        self.start.set_pv(self.start)
        fringe = PriorityQueue()
        fringe.put((self.start.get_thetaf(), random.random(), self.start))
        closed = []
        while not fringe.empty() :
            current = fringe.get()[2]
            if current.get_thetah() == 0 :
                while not fringe.empty() :
                    self.theta_updatevx(fringe,fringe.get()[2],current)
                path = []
                while current is not self.start :
                    path.append(current)
                    current = current.pv
                path.append(self.start)
                path.reverse()
                print('Path found')
                return path
                
            closed.append(current)
            for successor in self.find_neighbors(current) :
                if successor not in closed :
                    if not any(successor in item for item in fringe.queue) :
                        successor.set_g(math.inf)
                        successor.set_pv(None)
                    self.theta_updatevx(fringe, current, successor)
        print('No path found')
        return None


    def a_updatevx(self, pqueue, curr, succ) :       # update vertex method for A*
        if curr.get_g() + curr.get_distance(succ) < succ.get_g() :
            succ.set_pv(curr)
            pqueue.put((succ.get_f(), random.random(), succ))

    def theta_updatevx(self, pqueue, curr, succ) :       # update vertex method for Theta*
        if self.los(curr.pv, succ) :            # path 2
            if curr.pv.get_g() + curr.pv.get_distance(succ) < succ.get_g() :
                succ.set_pv(curr.pv)
                pqueue.put((succ.get_thetaf(), random.random(), succ))
        else :                                  # path 1
            if curr.get_g() + curr.get_distance(succ) < succ.get_g() :
                succ.set_pv(curr)
                pqueue.put((succ.get_thetaf(), random.random(), succ))

    def los(self, curr, succ) :     # line of sights method for Theta* update vertex method
        x0 = curr.get_x()
        x1 = succ.get_x()
        y0 = curr.get_y()
        y1 = succ.get_y()
        f = 0
        dx = x1 - x0
        dy = y1 - y0
        if dx < 0 :
            dx = -dx
            sx = -1
        else :
            sx = 1
        if dy < 0 :
            dy = -dy
            sy = -1
        else :
            sy = 1
        if dx > dy :
            while x0 != x1 :
                f += dy
                if f >= dx :
                    if self.cell_list[y0+int((sy-1)/2)][x0+int((sx-1)/2)].blocked == 1 :
                        return False
                    y0 += sy
                    f -= dx
                if f!=0 and self.cell_list[y0+int((sy-1)/2)][x0+int((sx-1)/2)].blocked == 1 :
                    return False
                if dy==0 and self.cell_list[y0][x0+int((sx-1)/2)].blocked == 1 and self.cell_list[y0-1][x0+int((sx-1)/2)].blocked == 1 :
                    return False
                x0 += sx
        else :
            while y0 != y1 :
                f += dx
                if f >= dy :
                    if self.cell_list[y0+int((sy-1)/2)][x0+int((sx-1)/2)].blocked == 1 :
                        return False
                    x0 += sx
                    f -= dy
                if f!=0 and self.cell_list[y0+int((sy-1)/2)][x0+int((sx-1)/2)].blocked == 1 :
                    return False
                if dx==0 and self.cell_list[y0+int((sy-1)/2)][x0].blocked == 1 and self.cell_list[y0+int((sy-1)/2)][x0-1].blocked == 1 :
                    return False
                y0 += sy
        return True
       
# Testing section




