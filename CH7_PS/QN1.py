# 1. Write a program to print multiplication table of a given number using for loop.

n= int (input ("Enter which no. of table you want : "))

for i in range (1,11):
    print (n , "X", i ,"=", i*n)
    i = i+1