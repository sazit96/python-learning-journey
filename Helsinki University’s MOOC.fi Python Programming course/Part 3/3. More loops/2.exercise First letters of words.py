text = input("Please type in a sentence: ")
sentence = text.split()
i = 0
while i < len(sentence):
    print(sentence[i][0])
    i += 1