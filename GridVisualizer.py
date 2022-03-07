from inspect import getargvalues
from tkinter import *
from turtle import color
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
import PathPlanning

root = Tk()

size_label = Label(root, text='Enter dimensions of the grid you would like to generate: ')
size_label.pack()
xlabel = Label(root, text='Enter x size:')
xlabel.pack()
xsize = Entry(root, width=10)
xsize.pack()
ylabel = Label(root, text='Enter y size:')
ylabel.pack()
ysize = Entry(root, width=10)
ysize.pack()

grid_obj = PathPlanning.Grid()              # creates new empty grid

def show_grid() :

    # Matplotlib grid creation

    PathPlanning.Grid.generate_grid(int(xsize.get()),int(ysize.get()))        # generates text file grid that takes in size values from entry widgets
    grid_obj.populate_grid('gridtext.txt')      # populates grid with previously generated text file
    path = grid_obj.a_star()                    # runs the A* algorithm on the populated grid and returns shortest path if found, and None if no path was found
    xvals = []
    yvals = []

    if path is not None :
        for i in path :
            xvals.append(i.x)
            yvals.append(i.y)


    fig, grid_plot = plt.subplots()
    grid_plot.invert_yaxis()

    plt.grid(visible=True)
    plt.xticks(range(grid_obj.dimensions[0]+2))     # changes the intervals of the x axis to 1
    plt.yticks(range(grid_obj.dimensions[1]+2))     # changes the intervals of the y axis to 1
    plt.hlines(range(1,grid_obj.dimensions[1]+2),1,grid_obj.dimensions[0]+1, color='black')     # creates the horizontal grid lines
    plt.vlines(range(1,grid_obj.dimensions[0]+2),1,grid_obj.dimensions[1]+1, color='black')     # creates the vertical grid lines
    for i in range(len(grid_obj.cell_list)) :
        for j in range(len(grid_obj.cell_list[0])) :
            if grid_obj.cell_list[i][j].blocked == 1 :
                cell_square = plt.Rectangle((grid_obj.cell_list[i][j].tl_vertex.x,grid_obj.cell_list[i][j].tl_vertex.y), 1, 1, fc='grey')
                plt.gca().add_patch(cell_square)


    plt.scatter([grid_obj.start.get_x(), grid_obj.goal.get_x()], [grid_obj.start.get_y(), grid_obj.goal.get_y()], c=['blue','red'])     # plots start and goal vertices as red and blue points respectively
    plt.plot(xvals,yvals, '--', c='red')      # plots path
    plt.show()


grid_gen = Button(root, text='Generate grid', command=show_grid)
grid_gen.pack()

# Vertex value finder

vertex_label = Label(root, text='Enter x and y coordinates of vertex you would like to calculate g, h, and f values for:')
vertex_label.pack()
xcoord_label = Label(root, text='Enter x coordinate of vertex:')
xcoord_label.pack()
xcoord = Entry(root, width=10)
xcoord.pack()
ycoord_label = Label(root, text='Enter y coordinate of vertex:')
ycoord_label.pack()
ycoord = Entry(root, width=10)
ycoord.pack()

glabel = Label(root)
hlabel = Label(root)
flabel = Label(root)
val_clicks = 0
def calculate_vals() :
    global val_clicks
    if val_clicks > 0 :     # checks if button has been pressed already and clears labels if it has been
        glabel.pack_forget()
        hlabel.pack_forget()
        flabel.pack_forget()
    if grid_obj.vertex_list[int(ycoord.get())][int(xcoord.get())].get_g() is None :
        gval = 'Vertex not expanded'
        fval = 'Vertex not expanded'
    else :
        gval = grid_obj.vertex_list[int(ycoord.get())][int(xcoord.get())].get_g()
        fval = grid_obj.vertex_list[int(ycoord.get())][int(xcoord.get())].get_f()
    hval = grid_obj.vertex_list[int(ycoord.get())][int(xcoord.get())].get_h()
    glabel.configure(text='g value: ' + str(gval))
    hlabel.configure(text='h value: ' + str(hval))
    flabel.configure(text='f value: ' + str(fval))
    glabel.pack()
    hlabel.pack()
    flabel.pack()
    val_clicks+=1
    

value_gen = Button(root, text='Calculate Values', command=calculate_vals)
value_gen.pack()

root.mainloop()