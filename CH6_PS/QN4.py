# 4. Write a program to find whether a given username contains less than 10 characters or not.


name = input ("Enter your username : ")

if len(name)>=10:
    print ("Valid ")
else :
    print ("Your username is not contain 10 character, try another")