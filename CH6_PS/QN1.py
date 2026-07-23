# 1. Write a program to find the greatest of four numbers entered by the user.

no1 = int (input ("Enter 1st no : "))
no2 = int (input ("Enter 2nd no : "))
no3 = int (input ("Enter 3rd no : "))
no4 = int (input ("Enter 4th no : "))

if (no1>no2)and (no1>no3) and (no1>no4):
    print ("Greater  no is :" , no1)
elif (no2>no1)and (no2>no3) and (no2>no4):
    print ("Greater  no is :" , no2)
elif (no3>no2)and (no3>no1) and (no3>no4):
    print ("Greater  no is :" , no3)
elif (no4>no2)and (no4>no3) and (no4>no1):
    print ("Greater  no is :" , no4)
