# Take input from user
x = int(input("Enter your x -> "))
y = int(input("Enter your y -> "))

# Compare x and y
if x > y:
    print("X is greater than Y")
elif x < y:
    print("Y is greater than X")
else:
    print("X and Y are equal")

# Check equality directly
if x != y:   # Not equal
    print("X and Y are not equal")
else:        # Equal
    print("X and Y are equal")
