import math

class Surface:
    @staticmethod
    def calculate_triangle(a,h):
        print(f"Surface: {a*h/2}")

    @staticmethod
    def calculate_rectangle(a,b):
        print(f"Surface: {a*b}")
    
    @staticmethod
    def calculate_circle(r):
        print(f"Surface: {math.pi*r**2}")

Surface.calculate_triangle(6,2)
Surface.calculate_rectangle(4,7)
Surface.calculate_circle(3)