# A* and BFS algorithms in AI
We have to find the path between 2 points on image. The user enters the image as well as the 2 points. Algorithms used are A* and BFS then the path will be drawn on the image.
# Getting Started
In order to work with images we will use PILLOW library for reading, editing and drawing the line. As well as numpy library to work with matrices. And math library to calculate the distance between the points.
## Prerequisites
First of all, we need to install the packages mentioned before pillow, numby and math.
# Read image
As mentioned before reading the image will be done using pillow library. In `main` function write the part of code bellow.
```
file = input("Plase enter image name: \n")
image = Image.open(file)
```
# Convert image to array
Before converting image pixels into array we need to change the dimensions of the image to be 1000x1000.
```
resized = image.resize((1000,1000))
resized.save(file)
```
Now we will use numpy library in order to make the image matrix as array.
```
data = np.asarray(resized, dtype='uint8')
```
# Finding the path
We have two different algorithms to find the path, A* and BFS.
## A* Algorithm
A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals. What A* Search Algorithm does is that at each step it picks the point according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. At each step it picks the point having the lowest ‘f’, and process that point.
* F is the total cost of the point.
* G is the distance between the current point and the start point.
* H is the heuristic — estimated distance from the current point to the end point.
### Pseudocode
We create two lists – Open List and Closed List.
```
1. Initialize the open list
2. Initialize the closed list
3. Put the starting point on the open list
4. Loop until you find the end (while the openList is not empty)
    * Get the current point. 
      let the currentPoint equal the point with the least f value,
      remove the currentPoint from the openList,
      add the currentNode to the closedList.
    * Found the goal
      if currentPoint is the goal,
            You've found the end! Backtrack to get path.
    * Generate children
      let the children of the currentPoint equal the adjacent points.
      for each child in the children
           * Child is on the closedList
             if child is in the closedList
                Continue to beginning of for loop
           * Create the f, g, and h values
             child.g = currentPoint.g + distance between child and current
             child.h = distance from child to end
             child.f = child.g + child.h
           * Child is already in openList
             if child.position is in the openList's points positions
                if the child.g is higher than the openList point's g
                    continue to beginning of for loop
           * Add the child to the openList
```
## BFS Algorithm
BFS is a traversing algorithm where we should start traversing from a selected point and traverse the graph layerwise thus exploring the neighbour points. We must then move towards the next-level neighbour points.
### Pseudocode
We create two lists – Explored List and Queue List.
```
1. Initialize the Explored list
2. Initialize the Queue list
3. Put the starting point on the Queue list
4. If start point equal to end point 
   return zero
5. Loop until you find the end (while the QueueList is not empty)
      * Pop the first path from the queue.
      * Get the last node from the path.
      * If point not in Explored list
         * Get neighbours.
         * Go through all neighbour points, construct a new path and push it into the Queue list.
         * If neighbour equal to end point
           return path
      * Mark point as explored
   In case there's no path between the 2 points
      retrun no path is found
```
# Results
After checking that everything is done let’s run python files.
## A* Algorithm's results
Run `astar.py` file and get the results below.
![Result1](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/astar1.png)
![Result2](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/astar2.png)
![Result3](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/astar3.png)
![Result4](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/astar4.png)
![Result5](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/astar5.png)

## BFS Algorithm's results
Run `bfs.py` file and get the results below.
![Result1](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/bfs1.png)
![Result2](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/bfs2.png)
![Result3](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/bfs3.png)
![Result4](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/bfs4.png)
![Result5](https://github.com/shazaalqays/AI-homework-1/tree/master/pics/bsf5.png)

# Conclusion
There is a time calculation for both A* and BFS algorithms this calculation shows that A* is much faster than BFS in my code they are following approx the same path but A* is faster in reaching the end point and more efficient.

# Prepared by
Chaza Alkis
