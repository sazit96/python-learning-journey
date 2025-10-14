word = input("Please type in a word: ")
character = input("Please type in a character: ")

i = 0
while i < len(word):
    if word[i] == character:
        if i + 3 <= len(word):
            print(word[i:i+3])
    i += 1