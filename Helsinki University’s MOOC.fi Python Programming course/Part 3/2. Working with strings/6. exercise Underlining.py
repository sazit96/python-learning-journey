while True:
    text = input("Please type in a string: ")
    if text == "":
        break
    print()
    
    print(text)
    
    i = 0
    underline = ""
    while i < len(text):
        underline += "-"
        i += 1
    print(underline)
