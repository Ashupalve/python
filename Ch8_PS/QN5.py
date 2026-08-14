n = int(input("Enter the number: "))
def star(n):
   for i in range(0,(6-n)): 
    print("*"* (3-i), end="")
    print("")

star(n)