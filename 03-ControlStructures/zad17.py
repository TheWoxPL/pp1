x = 5
y = 0

def print_quadrant(which_quadrant):
    print(f"Point P({x},{y}) is in the {which_quadrant} quadrant of the coordinate system")

def print_axis(axis):
    print(f"Point P({x},{y}) belongs to {axis} axis")

if x>0 and y>0:
    print_quadrant("first")
elif x<0 and y>0:
    print_quadrant("second")
elif x<0 and y<0:
    print_quadrant("third")
elif x>0 and y<0:
    print_quadrant("fourth")
elif x==0:
    print_axis("y")
elif y==0:
    print_axis("x")