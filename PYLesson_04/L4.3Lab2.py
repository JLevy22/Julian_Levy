print ("Lab 4.3 Part 2: Average")
print (" ")

avg=0.0
num1=float(input("Enter the value of a number:"))
num2=float(input("Enter the value of a number:"))
num3=float(input("Enter the value of a number:"))

def avgCalc():
    global avg
    avg=(num1+num2+num3)/3

def avgPrint():
    print("The average of ",num1,",",num2,", and ",num3," is {:0.5f}".format(avg))

avgCalc()
avgPrint()
