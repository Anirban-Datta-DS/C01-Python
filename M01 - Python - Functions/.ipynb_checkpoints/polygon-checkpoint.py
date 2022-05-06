'''
A module containing RegularPolygon class.
'''

import math
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

class RegularPolygon():
    
    '''
    A class that generates regular polygons of circumradius 1 unit.
    Enter number of sides to generate the polygon.
    
    Attributes
    ----------------
    n: int
            Defines the number of sides, mandatory, default = 6
    '''
    def __init__(self, n = 6):
        self.n = n
        
    @property
    def coordinates(self):
        '''
        Generate the list of coordinates from the number of sides. returns a list of coordinates (tuples).
        '''
        return [(math.cos(2*math.pi *i/self.n), math.sin(2*math.pi *i/self.n)) for i in range(self.n)]
    
    @property
    def side_length(self):
        '''
        Calcualates side length by applying Euclidean distance formula between 2 adjacent coordinates.
        '''
        return math.sqrt((self.coordinates[0][0] - self.coordinates[1][0])**2 + (self.coordinates[0][1] - self.coordinates[1][1])**2)
    
    @property
    def area(self):
        '''
        Calculates area of polygon from number of sides.
        '''
        polygon_area = round(((self.side_length)**2)*(self.n)/(4*math.tan(math.pi /self.n)), 4)
        return polygon_area
    
    def draw(self):
        '''
        Draws the polygon and its circum-circle.
        '''
        
        polygon = Polygon(self.coordinates)
        x,y = polygon.exterior.xy
        
        fig, ax = plt.subplots(figsize = (6, 6))
#         ax.set_aspect( 1 )
        
        plt.plot(x,y)
        plt.axvline(x=0, c="black", ls = '--', label="x=0")
        plt.axhline(y=0, c="black", ls = '--', label="y=0")
        
        Drawing_uncolored_circle = plt.Circle((0, 0), 1, fill = False, color="green", ls='--')
        plt.plot([0, self.coordinates[1][0]], [0, self.coordinates[1][1]], color='r', linestyle='-', linewidth=2)
        plt.plot(0,0, 'ro')
        plt.plot(self.coordinates[1][0],self.coordinates[1][1], 'ro')
        ax.add_artist(Drawing_uncolored_circle)
        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        
        plt.show()
        
    def __gt__(self, other):
        return self.area > other.area
    
    def __lt__(self, other):
        return self.area < other.area
        