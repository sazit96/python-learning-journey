word_store = ""
previous = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    word_store += word + " "
    previous = word

print(word_store)
