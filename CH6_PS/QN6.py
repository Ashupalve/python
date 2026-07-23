# Write a program to calculate the grade of a student from his marks from the following scheme
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# 40 – 50 => p
# <40 => F

marks = int (input ("Enter your marks :"))

if marks in range (90,101):
    print ("your grade is : EX")
elif marks in range (80,90):
    print ("Your grade is : A")
elif marks in range (70,80):
    print ("Your grade is : B")
elif marks in range (60,70):
    print ("Your grade is : C")
elif marks in range (50,60):
    print ("your grade is : D")
elif marks in range (40,50):
    print ("your grade is : P")
else:
    print("Your grade is : F \n", "You are fail")