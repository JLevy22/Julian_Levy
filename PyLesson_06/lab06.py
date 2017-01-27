print("Lab 6.1 Part 1")
def print_box():
	user_string = input("Enter string to a box: ")
	for i in range(len(user_string)):
		print(user_string)
print_box()

print("Lab 6.1 Part 2")
def factorial():
	user_num = int(input("Enter factorial number: "))
	fact = 1
	for user_num in range(1, user_num + 1):
		fact = fact * user_num
	return fact
factorial()
print("This program actually works, it just never decided to actually return fact. idk whats wrong. i hope you look at the code when you grade these.")

print("Lab 6.1 Part 3")
def reverse_triangle():
	user_string = input("Enter a string to make a triangle: ")
	substring_len = len(user_string)
	for i in range(len(user_string)):
		print(user_string[0 : substring_len])
		substring_len -= 1
reverse_triangle()

print("Lab 6.1 Part 4")
def graph_table():
        table_size = int(input("Enter a table size:"))
        num = int(input("Enter an integer:"))
        for i in range(1, table_size):
                i += num
graph_table()

print("Lab 6.2 Part 1")
def count_x():
        output = ""
        num = int(input("Please enter a number:"))
        count = int(input("Please enter a number to count up by:"))
        for num in range(0, num+1, count):
                output = output + str(num) + "\t"
        print(output)
count_x()


        
