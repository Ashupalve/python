# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft

class programmer :
    company = "Microsoft"
    def __init__(self, name , sallary , branch  , skills , address):

        self.name = name 
        self.sallary = sallary
        self.branch = branch
        self.skills = skills 
        self.address = address

P1 = programmer ("Ashwed", 1000000 ,"AI" , "Python Devloper , Cloud ", "Nashik")

print (f"{P1.name} , {P1.sallary}, {P1.skills}, {P1.branch}")
