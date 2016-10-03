print ("Lab 4.0 Part 2: ID Card")
print (" ")

def format (school,year):
    print ("{:>13}\t{:>13}".format(school,year))

fname=input ("Please enter your first name:")
lname=input ("Please enter your last name:")
title=input ("Please enter your title:")
school=input ("Which school are you attending:")
year=input ("Please enter the year:")
subject=input ("Which subject are you taking:")

print ("************************************")
format (school,year)
format (fname,lname)
format (title,subject)
print ("************************************")
