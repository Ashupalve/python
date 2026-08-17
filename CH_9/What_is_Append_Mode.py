#Append mode adds lines or data at last of file 
# and Write mode only writes means previous data delets and new data writs
#but append not delets previous data from file 
#ex
f = open("file.txt","a")       # "a" is for append mode 
add = ("\nits new data ")      # "\n" for data add at new line if we dont write \n then it writs from last character of file 
f.write(add)
f.close()
