from typing import cast,Any
import Rhino.Geometry as rg #type:ignore
import math

# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
x_points = cast(int, x_points)  # type: ignore
y_points = cast(int, y_points)  # type: ignore

#START CONDING HERE 
pointList1 = []

# Create points along the X-axis using the slider input "x_points"
for i in range(x_points):
    pt = rg.Point3d(i, 0, 0)
    pointList1.append(pt)
a = pointList1
    
#2. - create second series of points -
#create a second list of points  by copying the code above, but this time
#assign the Y coordinate of each point to a value that comes from an 
#external input which can be a slider in grasshopper called y_points
 

pointList2 = []
# Create points along the Y-axis using the slider input "y_points"
for i in range(y_points):
    pt = rg.Point3d(i, 15, 0)
    pointList2.append(pt)
b = pointList2


#3. - create lines from two serie of points - 
#initialize another empty list to store some lines
#make another for loop that iterates through each point in any of the list BY INDEX
#within this loop, make a line that draws from points in both lists with the same index
#and append that line to the line list. output the result
#hint: you only need one for loop for this

lineList = []

#your code here


c = lineList
#4. - create a circle from the first point of each list -
#initialize another empty list to store some circles    
#make another for loop that iterates through each point in any of the list BY INDEX
#within this loop, make a circle that draws from the first point in the list with the same index
#and append that circle to the circle list. output the result
#hint: you only need one for loop for this  
