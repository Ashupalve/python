# use comparison operator to find out whether a given variable a is greater than b or not  take a =34 & b= 80

a = 34 
b = 80
if (a>b):
    print (a , "Is greater than" , b)

else:
    print (a , "Not greater than" , b)

# now  will try own u1st sing a & b is input
a = int(input("Enter 1st no : "))
b = int(input("Enter 2 nd no : "))
if (a>b):
    print (a , "Is greater than" , b)

elif(a==b):
    print (a , "is equal to" , b)

else:
    print (b , "Not greater than" , a)

# a = int(input("Enter 1st no : "))
# b = int(input("Enter 2 nd no : "))
# print("a is greater than b ", a>b)