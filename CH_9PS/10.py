# 10. Write a program to wipe out the content of a file using python.

with open ("Q10.txt") as f:
    data = f.read()

print(data,"Before cleaning")

with open("Q10.txt","w")as f:
    f.write("")

with open ("Q10.txt") as f:
    data = f.read()

print(data,"After cleaning")