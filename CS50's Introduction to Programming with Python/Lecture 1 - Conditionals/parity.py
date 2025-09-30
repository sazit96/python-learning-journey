# Take input from the user
number = int(input("Enter a number -> "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
def iseven(n):
    return n % 2 == 0 
# True if n % 2 == 0 else False

def main(): 
    n = int (input ("Enter Number -> "))
    if iseven(n): print ("Even")
    else : print ("Odd");

main()