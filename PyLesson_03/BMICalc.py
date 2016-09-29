print ("Lesson 3 Lab Part 2")
print(" ")

def format (BMI):
    print ("{:4.2f}".format(BMI))

weight = float(input("Please enter your weight in pounds:"))
height = float(input("Please enter yur height in inches:"))

height2= height**2
BMI1= weight/height2
BMI2= BMI1*703

format ("Your BMI is:",BMI2)



