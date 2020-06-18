import os
import sys
import getopt

# Import necessary modules
import geopandas as gpd
import math 
from shapely.geometry import Polygon
from geopandas.tools import sjoin
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##########################
# A* search class
##########################

class A_star_search:
    
    def __init__(self, x_start, y_start, x_end, y_end, color_grid):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.color_grid = color_grid
        self.closed_list = {}
        self.open_list = {}

    def in_open_list(x,y):
        return '{},{}'.format(x,y) in self.open_list

    def in_close_list(x,y):
        return '{},{}'.format(x,y) in self.close_list

    def convert_key_to_coordinates(key):
        return [int(key.split(',')[0]), int(key.split(',')[1])]

    def hamming_distance(self, x, y):
        return abs(x - self.x_end) + abs(y - self.y_end)

    def checkopenlist(x_start, y_start, x_destination, y_destination, cost):
        if (self.in_open_list(x_destination, y_destination) and cost < self.open_list[[x_destination, y_destination]][0]) or \
                not self.in_open_list(x_destination, y_destination):
            self.open_list['{},{}'.format(x_destination, y_destination)] = (cost, (x_start, y_start))

    def search(self):   
        x = self.x_start
        y = self.y_start
        
        while True:
            if x == self.x_end and y == self.y_end:
                break
            
            ## build the cost function
            # diagonal path
            if self.color_grid[x][y] == 0 and not self.in_close_list(x-1, y+1):
                cost = 1.5 + self.hamming_distance(x-1, y+1)
                self.checkopenlist(x, y, x-1, y+1, cost, open_list)
            
            if self.color_grid[x-1][y-1] == 0 and not self.in_close_list(x-1,y-1):
                cost = 1.5 + self.hamming_distance(x-1, y-1)
                self.checkopenlist(x, y, x-1, y-1, cost, open_list)
            
            if self.color_grid[[x+1, y-1]] == 0 and not self.in_close_list(x+1,y-1):
                cost = 1.5 + self.hamming_distance(x+1, y-1)
                self.checkopenlist(x, y, x+1, y-1, cost, open_list)
            
            if self.color_grid[[x+1, y]] == 0 and not self.in_close_list(x+1,y):
                cost = 1.5 + self.hamming_distance(x+1, y)
                self.checkopenlist(x, y, x+1, y, cost, open_list)
            
            # horizontal straight lines
            if (self.color_grid[x][y] == 1 and self.color_grid[x+1][y] == 0) or \
                (self.color_grid[x][y] == 0 and self.color_grid[x+1][y] == 1) and \
                (not self.in_close_list(x,y+1)):
                cost = 1.3 + self. hamming_distance(x, y+1)
                self.checkopenlist(x, y, x, y+1, cost, open_list)
                    
            if (self.color_grid[x][y] == 0 and self.color_grid[x+1][y] == 0) and (not self.in_close_list(x,y+1)):
                cost = 1 + self. hamming_distance(x+1, y)
                self.checkopenlist(x, y, x, y+1, cost, open_list)

                
            if (self.color_grid[x][y-1] == 1 and self.color_grid[x+1][y-1] == 0) or (self.color_grid[x][y-1] == 0 \
                and self.color_grid[x+1][y-1] == 1) and not self.in_close_list(x,y-1) :
                cost = 1.3 + self. hamming_distance(x, y-1)
                self.checkopenlist(x, y, x, y-1, cost, open_list)
                
            if (self.color_grid[x][y-1] == 0 and self.color_grid[x+1][y-1] == 0) and not self.in_close_list(x,y-1):  
                cost = 1 + self. hamming_distance(x, y-1)
                self.checkopenlist(x, y, x, y-1, cost, open_list)
            
            # vertical straight lines
            if (self.color_grid[x][y] == 1 and self.color_grid[x][y-1] == 0) or (self.color_grid[x][y] == 0 \
                and self.color_grid[x][y-1] == 1) and not self.in_close_list(x-1,y) :
                cost = 1.3 + self. hamming_distance(x-1, y)
                self.checkopenlist(x, y, x-1, y, cost, open_list)     

                
            if (self.color_grid[x][y] == 0 and self.color_grid[x][y-1] == 0) and not self.in_close_list(x-1,y):
                cost = 1 + self. hamming_distance(x-1, y)
                self.checkopenlist(x, y, x-1, y, cost, open_list)   
                
            if (self.color_grid[x+1][y] == 1 and self.color_grid[x+1][y-1] == 0) or (self.color_grid[x+1][y] == 0\
                and self.color_grid[x+1][y-1] == 1) and not self.in_close_list(x+1,y):
                cost = 1.3 + self. hamming_distance(x+1, y)
                self.checkopenlist(x, y, x+1, y, cost, open_list)    
                  
            if (self.color_grid[x+1][y] == 0 and self.color_grid[x+1][y-1] == 0) and not self.in_close_list(x+1,y):        
                cost = 1 + self. hamming_distance(x+1, y)
                self.checkopenlist(x, y, x+1, y, cost, open_list)  

            return_list=[]
            return_list.append((self.x_end,self.y_end))
            while (self.x_start,self.y_start) not in return_list:
                new_x, new_y = int(self.closed_list['{},{}'.format(x,y)].split(',')[0]), int(self.closed_list['{},{}'.format(x,y)].split(',')[1])
                return_list.append((new_x, new_y))
                x,y = new_x, new_y

            return return_list

##########################
# Search Function
##########################

def search (starting_pt, end_pt, threshold, file_data = 'crime_dt.shp'):
    step = 0.002  # step used to define the areas of our grid (grid height = 0.002, grid width = 0.002)

    #  reading the data
    path = 'Shape/{}'.format(file_data)
    crime_dt = gpd.read_file(path)

    # print('starting point: {}, end_point: {}, threshold: {}'.format(starting_pt, end_pt, threshold))
    # print('Path : {}, step : {}'.format(path, step))

    #  xmin = -73.590, xmax = -73.550, ymax = 45.530, ymin = 45.490
    xmin, ymin, xmax, ymax = crime_dt.total_bounds

    if starting_pt[0] < ymin or starting_pt[0] > ymax or starting_pt[1] < xmin or starting_pt > xmax :
        sys.exit('point not in the area of interest')

    #  get rows and columns
    number_columns = math.ceil((xmax - xmin)/step)
    number_rows = math.ceil((ymax - ymin)/step)

    #  we create the grid matrix
    grid = [[0 for x in range(number_columns)] for y in range(number_rows)]

    #  we fill in our grid
    for index in range(len(crime_dt)):
        latitude = crime_dt['geometry'][index].x
        longitude = crime_dt['geometry'][index].y
        i = (number_rows-1)-int((longitude-ymin)//step)  # had to invert to fit more with the git example
        j = int((latitude-xmin)//step)
        grid[i][j] += 1  # might be possible to add weights based on the felony committed

    # we find the threshold in terms of criminal rate value
    sorted_grid_list = []
    for i in range(0,number_rows):
        for j in range(0,number_columns):
            sorted_grid_list.append(grid[i][j])
    sorted_grid_list.sort(reverse = True)
    threshold_high_crime = sorted_grid_list[int((1-threshold)*len(sorted_grid_list))]

    color_grid = [[0 for x in range(number_columns)] for y in range(number_rows)]
    for i in range(0,number_rows):
        for j in range(0,number_columns):
            if grid[i][j] > threshold_high_crime:
                color_grid[i][j] = 1

    star_search = A_star_search(starting_pt[0], starting_pt[1], end_pt[0], end_pt[1], color_grid)
    list_points = star_search.search()

    colors = 'purple yellow'.split()
    cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
    plt.imshow(color_grid, cmap=cmap, interpolation='none', extent=[ymin,ymax,xmax,xmin])
    point_a = list_points[0]
    for point in list_points:
        point_b = point
        plt.plot((point_a[0]+1,point_b[0]+1),(point_a[1],point_b[1]),'r')
        point_a = point
    plt.show()


##########################
#  User Interface
##########################

command_line_help = '''
possible arguments :
-f OR --file : name of the file you want to use. (default : crime_dt.shp)
-s OR --start : point you want to start from [separator is a comma](default : None)
-e OR --end : point you want to reach [separator is a comma](default : None)
-t OR --threshold : threshold of crime rate you want to use [0,1](default : 0.5)
--step : step you want to determine the area (default : 0.002)
'''

commands_input = '''
Command (separator for points coordinates is a comma):
- search [starting_point] [end_point] [threshold]
- exit
'''

if __name__ == '__main__':

    arg = sys.argv[1:]

    # no command_line argument, dynamic user interface
    if len(arg)==0:
        try:
            while True:
                print(commands_input)
                command = str(input('Your Command > '))
                command_split = command.split(' ')
                try:
                    main_command = command_split[0]
                    if main_command == 'search' :
                        starting_pt = command_split[1].split(',')
                        end_pt = command_split[2].split(',')
                        threshold = float(command_split[3])
                        if len(starting_pt) < 2 or len(end_pt) < 2:
                            print('Invalid number of coordinates.')
                            continue
                        if threshold < 0 or threshold > 1 :
                            print('Threshold outside of bounds : [0,1]')
                            continue
                        starting_pt = [float(starting_pt[0]),float(starting_pt[1])]
                        end_pt = [float(end_pt[0]),float(end_pt[1])]
                        search(starting_pt,end_pt,threshold)
                    elif main_command == 'exit':
                        print('<< Exiting...')
                        break
                    else:
                        print('Invalid command')
                        print('You entered {}'.format(command_split))
                except IndexError:
                    print('Invalid command / number of parameters')
                    print('You entered {}'.format(command_split))
        except (KeyboardInterrupt, SystemExit, SystemError):
            print('Forced shutdown')

    # using command line arguments 
    else :
        file_data = 'crime_dt.shp' 
        start = None
        end = None
        threshold = 0.5

        try:
            args, vals = getopt.getopt(arg,"hf:s:e:t:",["help","file=","start=","end=","threshold="])
        except getopt.error as err:
            sys.exit(str(err) + 'use -h for help')

        for curr_arg, curr_val in args:
            if curr_arg in ("-h", "--help"):
                print(command_line_help)
                sys.exit()
            if curr_arg in ("-f","--file"):
                file_data = curr_val
            if curr_arg in ("-s","--start"):
                start = curr_val.split(',')
                if len(start) < 2:
                    sys.exit('Error : invalid start coordinates (separator is a comma)')
                start = [float(start[0]), float(start[1])]
            if curr_arg in ("-e","--end"):
                end = curr_val.split(',')
                if len(end) < 2:
                    sys.exit('Error : invalid end coordinates')
                end = [float(end[0]), float(end[1])]
            if curr_arg in ("-t","--threshold"):
                threshold = float(curr_val)
        
        if start and end :
            search(start, end, threshold, file_data)
        else:
            sys.exit('You need to enter coordinates for starting and ending points (separated by a comma)')

