# 6. Write a python function which converts inches to cms.

inch= float(input("Enter the value of inches you want to convert into cm :"))
def inch_into_cm(inch):
    cm = inch * 2.54
    print (inch,"=",cm, "cm")

inch_into_cm(inch)