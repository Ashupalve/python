# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.


sub1 = int(input("Enter marks of 1st sub :"))
sub2 = int(input("Enter marks of 2nd sub :"))
sub3 = int(input("Enter marks of 3rd sub :"))

total_obtained = sub1+ sub2 +sub3
total =300
percentage = (total_obtained/total)*100

if percentage >=40 and sub1 >=33 and sub2>=33 and sub3 >=33:
    print ("Congrats your passed with percentage :",percentage)
else :
    print ("Your aree failed ,try agian with more study","\n","Your percentage are :",percentage)