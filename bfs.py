from PIL import Image, ImageDraw
from numpy import asarray
import numpy as np
import math
import timeit

def getadjacent(n):
    x , y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def evaluate(ne,end):
    min = 0
    pointis = ne[0]
    for p in ne:
        # d = int(math.sqrt(((p[0]-end[0])**2)+((p[1]-end[1])**2)))
        d = abs(p[0]-end[0]) + abs(p[1]-end[1])
        # print(d)
        if d < min:
            min = d
            pointis = p
            # print(pointis)
    return pointis

def bfs_shortest_path(data, start, end):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # print(queue)

    # return path if start is goal
    if start == end:
        return '0'

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        # print(queue)
        path = queue.pop(0)
        # print(path)
        # get the last point from the path
        point = path[-1]
        # point = path[0]
        # print(point)
        if point not in explored:
            neighbours = getadjacent(point)
            # print(neighbours)
            # go through all neighbour points, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                # print(new_path)
                new_path.append(neighbour)
                # print(new_path)
                queue.append(new_path)
                # print(queue)
                # return path if neighbour is goal
                if neighbour == end:
                    # print(new_path)
                    return new_path

            # mark point as explored
            explored.append(point)
            # print(explored)

    # in case there's no path between the 2 points
    return "So sorry, but a connecting path doesn't exist :("


def main():

    file = input("Plase enter image name: \n")
    image = Image.open(file)

    startt = timeit.default_timer()

    resized = image.resize((1000,1000))
    resized.save(file)

    data = np.asarray(resized, dtype='uint8')

    tdata = data.transpose()

    start = (500,310)
    end = (600,400)

    path = bfs_shortest_path(tdata,start, end)
    print(path)

    stop = timeit.default_timer()
    print('Time: ', stop - startt)

    draw = ImageDraw.Draw(resized)
    draw.line((start, end), fill=128)
    resized.show()

if __name__ == '__main__':
    main()
