
def print_box():
	user_string = input("Enter string to a box: ")
	for i in range(len(user_string)):
		print(user_string)

def factorial():
	user_num = int(input("Enter factorial number: "))
	fact = 1
	for i in range(user_num):
		fact = fact * (i + 1)
	return fact

def reverse_triangle():
	user_string = input("Enter a string to make a triangle: ")
	substring_len = len(user_string)
	for i in range(len(user_string)):
		print(user_string[0 : substring_len])
		substring_len -= 1

def graph_table():
	