print ("Lab 4.1 Part 1: Compound Intrest")
print (" ")

def format (stat,A):
    print ("{:20}{:<10.2f}$".format (stat,A))


r=float(input("What is the intrest rate:"))
p=float(input("What is the principal amount:"))
n=float(input("How many times is it compounded per year:"))
t=float(input("How many years:"))
print (" ")

A1= 1+r/n
A2= n*t
A3= A1**A2
A4= A3*p
T= t*12
A5= A4/T

format("The total amount is:",A5)



