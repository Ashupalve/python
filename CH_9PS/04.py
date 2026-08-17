'''4. A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file
'''

word = "Donkey"
with open ("QN4.txt","r") as f :
    data = f.read()

Correct = (data.replace(word, "#####"))

with open ("QN4.txt","w") as f :
    f.write(Correct)

# word = "Donkey"

# with open("QN4.txt", "r") as f:
#     content = f.read()

# contentNew = content.replace("######",word)

# with open("QN4.txt", "w") as f:
#     f.write(contentNew)