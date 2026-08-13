# 1. Write a program using functions to find greatest of three numbers.


def greatest_no (a,b,c):
    if a>b and a>c :
        print(a,"Is greatest no ")
    elif b>a and b>c :
        print (b,"Is greatest NO.")
    else:
        print (c,"Is greatest NO.")

a = int (input("Enter 1st no.)"))
b = int (input("Enter 2nd no.)"))
c = int (input("Enter 3rd no.)"))

greatest_no(a,b,c)