import math

from constants import *

# Euclidean distance formula for 2d space
def calc_dist(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Returns direction of 2 objects
def calc_dir(x1, x2):
    if x1 > x2:
        return RIGHT
    else:
        return LEFT
