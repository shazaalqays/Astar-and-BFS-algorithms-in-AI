# AI-homework-1
We have to find the path between 2 points on image. The user enters the image as well as the 2 points. Algorithms used are A* and BFS then the path will be drawn on the image.
# Getting Started
In order to work with images we will use PILLOW library for reading, editing and drawing the line. As well as numpy library to work with matrices. And math library to calculate the distance between the points.
## Prerequisites
First of all, we need to install the packages mentioned before pillow, numby and math.
# Read image
As mentioned before reading the image will be done using pillow library. In `main` function write the part od code bellow.
```
file = input("Plase enter image name: \n")
image = Image.open(file)
```
# Convert image to array
Before converting image pixels into array we need to chane the dimensions of the image to be 1000x1000.
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
* Initialize the open list
* Initialize the closed list
* Put the starting point on the open list
* Loop until you find the end (while the openList is not empty)
 **
