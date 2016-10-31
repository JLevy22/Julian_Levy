print("Lab 4.3 Part 4: Circle")
print(" ")

area=0.0
r=float(input("What is the radius of the circle?"))

def calcArea():
    global area
    area=(r*(3.14**2))

def areaPrint():
    print("The area of a circle with a radius of ",r," is {:0.5f}.".format(area))

calcArea()
areaPrint()
