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

