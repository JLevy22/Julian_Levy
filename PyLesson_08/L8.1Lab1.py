print("Lab 8")
print("Lab 8.1 Part 1:")
def underscore():
	sentence = input("Enter a sentence to underscore:")
	return replace(sentence)

def replace(sentence):
	space = sentence.find(" ")
	if space == -1:
		return sentence
	else:
		return replace(sentence[0:space] + "_" + sentence[space + 1:])
underscore()

print("Lab 8.1 Part 2:")
def center():
        word1 = input("Please enter a word:")
        word2 = input("Please enter a word:")
        word3 = input("Please enter a word:")
        def makeCenter(word1, word2, word3):
                if len(word) >= 20
                        return word
                else:
                        word += " " + word + " "
center()
