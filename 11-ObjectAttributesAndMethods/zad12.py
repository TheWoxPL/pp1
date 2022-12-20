import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other_point):
        if self.x==other_point.x and self.y==other_point.y:
            return "Distance between them is 0"
        else:
            return f"Distance between them is {math.sqrt((other_point.x-self.x)**2+(other_point.y-self.y)**2)}"

point1=Point(0,0)
point2=Point(1,1)
print(point1==point2)