# 8. Write a program to make a copy of a text file “this.txt”

with open ("this.txt") as f:
    data = f.read()

with open("Copy_this.txt","w") as f:
    f.write(data)