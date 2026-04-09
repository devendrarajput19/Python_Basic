class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    
    def is_square(self):
        return self.length == self.width
    
    def display(self):
        print(f"Length = {self.length}")
        print(f"Width = {self.width}")
        print(f"Area = {self.calculate_area()}")
        print(f"Perimeter = {self.calculate_perimeter()}")
        print(f"Is Square = {self.is_square()}")

length = float(input("Enter Length = "))
width = float(input("Enter width = "))

rect = Rectangle(length, width)
rect.display()
