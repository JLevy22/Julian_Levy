print ("Lab 4.2 Part 1: Rectangle")
print (" ")

def format(perim,null):
    print ("{:<10.5f}{:35}".format(perim,null))

length = float(input("What is the length of the rectangle:"))
width = float(input("What is the width of the rectangle:"))

recPerim = length+length+width+width

format (recPerim," is the perimiter of your rectangle.")
