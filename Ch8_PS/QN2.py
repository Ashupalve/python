# 2. Write a python program using function to convert Celsius to Fahrenheit.


def celsius_fahrenheit(n):
    far =((n*1.8)+32)
    print(n,"celsius = ",far,"Fahrenheit")

n = int (input ("Enter celsius for converting:"))

celsius_fahrenheit(n)