print("Lab 4.3 Part 3: Cube")
print(" ")

sa=0.0
side=float(input("What is the length of the side of the cube?"))

def calcSA():
    global sa
    sa= 6*(side**2)

def printSA():
    print("The surface area of a cube with sides of",side," is {:0.5f}.".format(sa))

calcSA()
printSA()
