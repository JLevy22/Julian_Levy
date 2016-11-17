print("Lesson 6.1 Part 3: Reverse Triangle")

word= input("Please enter a word:")

def revTri():
    for i in range(len(word),0,-1):
        print(word[0:i])

revTri()
