# ----------------------------
# WHILE LOOP EXAMPLES
# ----------------------------
i = 5
while i != 0:  # loop until i becomes 0
    print("Sazit")
    i = i - 1  # decrease i by 1 each time

i = 0
while i < 3:   # run while i is less than 3
    print("Maew")
    i += 1     # same as i = i + 1


# ----------------------------
# FOR LOOP EXAMPLES
# ----------------------------
for i in [0, 1, 2]:   # loop over list items
    print("Oi")

for i in range(3):    # range(3) = 0,1,2
    print("Oi")

for _ in range(4):    # underscore = we don’t use the loop variable
    print("lets GO")

print("GO \n" * 3, end="")  # print "GO" 3 times with new lines


# ----------------------------
# WHILE LOOP WITH USER INPUT
# ----------------------------
while True:
    n = int(input("How many times you want to Maew -> "))
    if n > 0: break  # stop only if user enters positive number

for _ in range(n): 
    print("Maew")


# ----------------------------
# FUNCTIONS EXAMPLE
# ----------------------------
def main():
    number = get_number()  # ask for valid number
    maew(number)           # print Maew that many times

def get_number():
    while True:
        n = int(input("Enter Your Number => "))
        if n > 0:          # only positive allowed
            return n        # return number once valid

def maew(count):
    for _ in range(count): # print Maew 'count' times
        print("-Maew-")

main()
