print ("Lesson 3 Lab Part 3")
print (" ")

print ("Think of any 2 digit number, it doesnt matter the size as long as it is 2 didgits")

num = int(input("What is the number?:"))
digit1 = int(input("What is the first digit?:"))
digit2 = int(input("what is the second digit:"))

s1 = digit1+digit2
s2 = num-s1
print (s2)
print ("What just happened was I took the first number and subtracted it by them sum of its digits.")

dig = int(input("Now enter the first digit of the new number:"))
dig2 = int(input("Enter the second digit of the new number:"))

s3 = dig+dig2
print (s3)
print ("After repeating that same step with the new number, you get 9. If you do these 2 steps with any 2 digit number you will always get 9.")
