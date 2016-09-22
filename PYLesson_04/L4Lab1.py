print ("Lab Part 1:Receipt")
print (" ")

def format (item,price):
    print ("{:>15}\t{:10.2f}".format(item,price))
    
item1=input("Please enter the first item:")
item1price=float(input("Please enter the price:"))
item2=input("Please enter the second item:")
item2price=float(input("Please enter the price:"))
item3=input("Please enter the third item:")
item3price=float(input("Please enter the price:"))

subtotal= item1price+item2price+item3price
tax= subtotal*.08
total= tax+subtotal

print ("__________<Receipt>___________")
format (item1,item1price)
format (item2,item2price)
format (item3,item3price)
print (" ")
format ("Subtotal:", subtotal)
format ("Tax:", tax)
format ("Total:", total)
print ("______________________________")
