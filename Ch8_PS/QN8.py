# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range (1 ,11):
        print (n ,"X", i,"=",n*i)

n = int (input("Enter a no. which you want to make table"))
table(n)