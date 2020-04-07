# AI-homework-1
We have to find the path between 2 points on image. The user enters the image as well as the 2 points. Algorithms used are A* and BFS then the path will be drawn on the image.
# Getting Started
In order to work with images we will use PILLOW library for reading, editing and drawing the line. As well as numpy library to work with matrices. And math library to calculate the distance between the points.
## Prerequisites
First of all, we need to install the packages mentioned before pillow, numby and math.
# Read image
As mentioned before reading the image will be done using pillow library.
`file = input("Plase enter image name: \n")`
`image = Image.open(file)`
