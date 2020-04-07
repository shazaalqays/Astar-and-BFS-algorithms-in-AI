from PIL import Image, ImageDraw
from numpy import asarray
import numpy as np
import timeit

class Point():
    """A Point class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(resized, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given image"""

    # Create start and end node
    start_point = Point(None, start)
    start_point.g = start_point.h = start_point.f = 0
    end_point = Point(None, end)
    end_point.g = end_point.h = end_point.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start point
    open_list.append(start_point)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current point
        current_point = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_point.f:
                current_point = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_point)

        # Found the goal
        if current_point == end_point:
            path = []
            current = current_point
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get point position
            point_position = (current_point.position[0] + new_position[0], current_point.position[1] + new_position[1])

            # Make sure within range
            if point_position[0] > (len(resized) - 1) or point_position[0] < 0 or point_position[1] > (len(resized[len(resized)-1]) -1) or point_position[1] < 0:
                continue

            # Create new point
            new_point = Point(current_point, point_position)

            # Append
            children.append(new_point)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_point.g + 1
            child.h = ((child.position[0] - end_point.position[0]) ** 2) + ((child.position[1] - end_point.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_point in open_list:
                if child == open_point and child.g > open_point.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    file = input("Plase enter image name: \n")
    image = Image.open(file)

    startt = timeit.default_timer()

    resized = image.resize((1000,1000))
    resized.save(file)

    data = np.asarray(resized, dtype='uint8')

    start = (600,840)
    end = (800,325)

    path = astar(data,start, end)
    print(path)

    stop = timeit.default_timer()
    print('Time: ', stop - startt)

    draw = ImageDraw.Draw(resized)
    draw.line((start, end), fill=225)
    resized.show()


if __name__ == '__main__':
    main()
