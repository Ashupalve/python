# Write a recursive function to calculate the sum of first n natural numbers.

n = int (input("Enter a how many no. you want to sum:"))
def sum (n):
    sum=0
    for i  in range (0,n+1):
        sum=sum+i
        i = i+1
    print("Sum of first", n, "natural numbers is:", sum)

sum(n)
