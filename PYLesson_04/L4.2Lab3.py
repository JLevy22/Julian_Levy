print ("Lab 4.2 Part 3: Cube")
print (" ")

    
side=float(input("Please enter the lenght of a side of a cube:"))

def calcSurf(side):
    return 6*(side**2)

def numPrint(side):
    print ("The surface are of a cube which sides are",side,"in length is {:0.5}".format(calcSurf(side)))
    
numPrint(side)

