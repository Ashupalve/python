# 9. Write a program to find out whether a file is identical and matches the content of another file

with open("this.txt")as f :
    data = f.read()

with open("Copy_this.txt")as f:
    data2 = f.read()

if data == data2:
    print(f"Both files are same and their content also same")
else:
    print("Both files have different content")