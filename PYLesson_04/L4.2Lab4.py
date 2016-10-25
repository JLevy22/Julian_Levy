print ("Lab 4.2 Part 4: Circle")
print (" ")

area=0.0
r=float(input("Please enter the radius of a circle:"))

def calcArea():
    global area
    area= 3.14*(r**2)

def numPrint():
    print("The area of a circle with a radius of",r,"is {:0.5f}".format(area))
calcArea()
numPrint()
