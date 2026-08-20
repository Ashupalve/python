# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.


class claculator :
    def __init__(self , num ):
        self.num = num
    def square(self):
        square = self.num * self.num
        print(f"Square of {num} is = {square}")
    def cube (self):
        cube = self.num*self.num*self.num
        print( f"Cube Of {num} Is = {cube}")
    def squareroot (self):
        squareroot = self.num**1/2
        print( f"Squareroot of {num} is = {squareroot}")


num = int (input("Enter number wich you want to calcumate: "))
a=claculator(num)
a.square()
a.cube()
a.squareroot()