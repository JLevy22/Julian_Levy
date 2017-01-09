def digitAdder():
	number = int(input("Enter a number to do stuff to:"))
	sum_num = 0
	num = number
	while num > 0:
		sum_num += num % 10
		num = int(num / 10)
	print("The sum of the digits in ", number," is ", sum_num)

