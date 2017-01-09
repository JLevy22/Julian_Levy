def underscore():
	sentence = input("Enter a sentence to underscore:")
	return replace(sentence)

def replace(sentence):
	space = sentence.find(" ")
	if space == -1:
		return sentence
	else:
		return replace(sentence[0:space] + "_" + sentence[space + 1:])