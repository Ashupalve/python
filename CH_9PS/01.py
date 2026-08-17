# 1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
# contains the word ‘twinkleʼ

with open ("poem.txt") as f:
    poem = f.read()
    word = input ("Which word you want to find in file :")
    if word in poem:
        print (f"{word} is present in poem")
    else :
        print (f"{word} is not present in poem")
