# Write a program to find whether a given number is prime or not

a = int (input("Enter a no. which have you check it is prime or not :"))

if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")