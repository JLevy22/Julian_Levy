print ("Lab 4.3 Part 1: Rectangle")
print (" ")

perim=0.0
l=float(input("Enter the length of the rectangle in feet:"))
w=float(input("Enter the width of the rectangle in feet:"))
h=float(input("Enter the hight of the rectangle in feet:"))

def calcPerim():
    global perim
    perim= (2*l)+(2*w)

def perimPrint():
    print ("The rectangle is {:0.5f} feet around.".format(perim))

calcPerim()
perimPrint()
