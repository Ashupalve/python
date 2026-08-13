# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int (input("Enter a no. :"))

i = 1
sum =0
while (i<=n):
    sum = sum +i
    i = i+1
print("sum of first",n,"Natural no. is:",sum)
