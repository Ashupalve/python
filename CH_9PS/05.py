# 5. Repeat program 4 for a list of such words to be censored.

word = "Donkey"
with open ("QN4.txt","r") as f :
    data = f.read()

Correct = (data.replace(word,"#" * len(word)))

with open ("QN4.txt","w") as f :
    f.write(Correct)