print ("Lab 4.1 Part 1: Compound Intrest")
print (" ")

def format (stat,A,dollars):
    print ("{:20}{:<10.2f}{:<2}".format (stat,A,dollars))

dollars= ("$")
r=float(input("What is the intrest rate:"))
p=float(input("What is the principal amount:"))
n=float(input("How many times is it compounded per year:"))
t=float(input("How many years:"))
print (" ")

A1= 1+r/n
A2= n*t
A3= A1**A2
A4= A3*p


format("The total amount is:",A4,dollars)

