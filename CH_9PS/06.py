# 6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.

with open("log.txt") as f :
    data = f.read()

if "Python" in data:
    print("Python is present in log.txt")
else:
    print("Python is not present in log.txt")