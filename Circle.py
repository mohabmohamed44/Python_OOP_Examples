import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
# Example usage
radius = float(input("Enter the radius of the Circle: "))

# Circle Object with Provided radius
circle  = Circle(radius)

# Calculate the area and perimeter
perimeter = circle.calculate_area()

area = circle.calculate_perimeter()

print("Perimeter of the Circle is: ", perimeter)
print("Area of the Circle is: ", area)