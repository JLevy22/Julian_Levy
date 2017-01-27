print("Lab 7.1 Part 1")
def digitAdder():
	number = int(input("Enter a number to do stuff to:"))
	sum_num = 0
	num = number
	while num > 0:
		sum_num += num % 10
		num = int(num / 10)
	print("The sum of the digits in ", number," is ", sum_num)
digitAdder()

print("Lab 7.1 Part 2")
def averageDigits():
        digits = 0
        average = 0
        number = int(input("Please enter a number:"))
        def avDigits():
                num = number
                while num > 0:
                        digits += 1
                        average += num % 10
                        num = num / 10
        print("The average of the digits in ", number," is ", average,".")
averageDigits()

print("Lab 7.1 Part 3")
def reverseNumber():
        number = int(input("Please enter a number:"))
        num = number
        rev = 0
        def getReverse():
                while num > 0:
                     rev += rev * 10
                     rev += num % 10
                     num = num / 10
        print(number,"reversed is:",rev)
reverseNumber()

print("Lab 7.1 Part 4")
def replaceAts():
        sentence = input("Please enter a sentence:")
        top = 0
        def replace():
                while top < sentence.count("a") > 0:
                        sentence = sentence[0 : sentence.index("@")] + sentence[sentence.index("@")+1 : len(sentence)]
        print("With a's replaced the sentece looks like:",sentence)     
replaceAts()
