num = int(input("Please type in a number: "))

i = 1
while i <= num:
    if i + 1 <= num:
        print(i + 1)
        print(i)
        i += 2
    else:
        print(i)
        i += 1