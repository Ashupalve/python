#write a program to fill in a letter template given blow with name and date 
'''letter = dear <name > 
                    you are selected 
                    <date>'''
name = input("Enter your name for checking list : ")
selected_studants=["Ashwed" ,"Umesh" ,"Rushikesh" ,"Atharva", "Shubham"]
letter = '''Dear <|Name|>,
            your are selected! 
            <|Date|>'''
if name in selected_studants:
    # print ("hii")
    print (letter .replace("<|Name|>", name ).replace("<|Date|>", "23 July 2026"))

else :
    print ("Sorry but ,Your are not selected , Try next time ")