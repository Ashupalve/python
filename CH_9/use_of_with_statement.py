
# "with" is use for not typing f.close  it automatic closes the file at the end of "with" statement

f = open ("file.txt")
Data = f.read()
print (Data)

# we writh the above code using "with" statement like:

with open("file.txt") as f:
    print(f.read())

