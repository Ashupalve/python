
# a = (input("give a no. "))
# print(type(a))               # input is always string type but we change the type of data using type casting ex 
# a = int(a)
# print(type(a))

# a = 10.25     # it is float type of data or it is decimal type of data

# a = True    # it is boolean type of data, we use it for questions like true or false, yes or no, 1 or 0, etc.

# a = "Jai shree krishna"   # it is string type of data, we use it for text or words or sentences, etc.

# # these are main types of data we use in python 

# let we try a example which contain all data types 

name  = (input ("Enter your name:"))

roll = int(input("Enter your roll number:"))  #in this line we get input form user and it convert into int formate 

cgpa = float(input("Enter your CGPA :"))  # in this line we get input form user and it convert into float formate

sub1 = int(input("Enter your DBMS marks:"))  # in this line we get input form user and it convert into int formate

sub2 = int(input("Enter your HCI marks:"))  # in this line we get input form user and it convert into int formate

sub3 = int(input("Enter your WT marks:"))  # in this line we get input form user and it convert into int formate

sub4 = int(input("Enter your AI marks:"))  # in this line we get input form user and it convert into int formate
sub5 = int(input("Enter your CN marks:"))  # in this line we get input form user and it convert into int formate

total_marks = 350

total_obtained = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total_obtained / total_marks) * 100

print("your percentage are :", percentage)


if percentage >=30:
    print(" Congrats you are pass")
else:
    print("Sorry but you are fail, better luck next time")
print ("We also find your percentage using your cgpa it is :", cgpa * 9.5)

print("Thanks for using this program, Jai shree krishna (dandvat)")

print ("It is devloped by : Ashwed Palve")