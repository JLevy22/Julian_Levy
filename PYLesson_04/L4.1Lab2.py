print ("Lab 4.1 Part 2: Subwoofer Boxes:")
print (" ")

def format (volume):
    print ("{:10.4f}".format (volume))

h= float(input("Please enter the hight in inches:"))
l= float(input("Please enter the length in inches:"))
w= float(input("please enter the width in inches:"))

inchvol = h*l*w
format ("The volume in cubic inches is:",inchvol)

cubef = 12*12*12

feetvol = inchvol/cubef
format ("The volume in cubic feet is:",feetvol)
