from random import randint

print("Lab 1")
def random_numbers():
	numsList = []
	for i in range(0, 4):
		numsList.append([])
		for j in range(0, 4):
			numsList[i].append(randint(1, 100))

	for nums in numsList:
		output = ""
		for num in nums:
			output += str(num) + " "
		print(output)
random_numbers()

print("Lab 2")
def strings():
	go = input("Please enter 16 words/strings: ")
	spList = go.split(" ")
	wordsList = []
	spot = 0
	for i in range(0, 4):
		output = ""
		wordsList.append([])
		for j in range(0, 4):
			wordsList[i].append(spList[spot])
			output += wordsList[i][j] + " "
			spot += 1
		print(output)
strings()

print("Lab 3")
def x_and_o():
	xAndO = []
	for i in range(0, 4):
		xAndO.append([])
		for j in range(0, 4):
			switch = randint(0, 1)
			if switch is 1:
				xAndO[i].append("X")
			else:
				xAndO[i].append("O")
	for values in xAndO:
		output = ""
		for value in values:
			output += value
		print(output)
x_and_o()

print("Lab 4")
