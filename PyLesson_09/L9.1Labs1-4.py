from random import randint

print("Lab 1")
def reverse_word():
	words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	print("In order...")
	for word in words:
		print(word)
	print()
	print("Reversed...")
	words.reverse()
	for word in words:
		print(word)
reverse_word()

print("Lab 2")
def first_letter():
	words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	for word in words:
		print(word[0:1])
first_letter()

print("Lab 3")
def average_num():
	numbers = []
	for num in range(10):
		numbers.append(randint(1, 100))
	print("Numbers...")
	output = ""
	for num in numbers:
		output += str(num) + " "
	print(output)
	print()
	print("The average of the above numbers is... " + str(average(numbers)))

def average(nums):
	sum = 0
	for num in nums:
		sum += num
	return sum/len(nums)
average_num()
average()

print("Lab 4")
