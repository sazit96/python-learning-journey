number = int(input("Please type in a year: "))

if number % 400 == 0:
    print("That year is a leap year.")
elif number % 100 == 0:
    print("That year is not a leap year.")
elif number % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
