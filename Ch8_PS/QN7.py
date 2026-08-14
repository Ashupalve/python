l = ["Ashu","Ashwed","Ash"]
word=input ("Enter which word you want to delete from list :")
def remove_specific_word(l,word):
    if word in l:
        l.remove(word)
        print (word,"is deleted from list")
    else:
        print (word,"is not present in list")
remove_specific_word(l,word)