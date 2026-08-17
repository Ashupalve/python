# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old



def table(n):
    for i in range(1 , 11):
        print (f"{n} X {i} = {n*i}")

for n in range(2, 21):
   Table = ""
   for i in range(1 , 11):
    Table += f"{n} X {i} = {n*i}\n"
   print (Table)
   with open (f'Tables_QN3/table_{n}.txt' , "w") as f :
       f.write(f"Table of {n}\n")
       f.write(f"{Table}\n")
       
