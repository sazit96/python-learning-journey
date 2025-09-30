# Define a function to greet a person
def greet_user(username):
    print("Hello", username)

# Ask for the user's name
user_name = input("What's your name? ")

# Call the function with the user's name
greet_user(user_name)


# Function to calculate and print sum
def calculate_sum(number_a, number_b):
    print("Sum:", number_a + number_b)

# Take user inputs
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# Call the function
calculate_sum(first_number, second_number)

Main function
def main():
    number = int(input("Enter a number to square: "))
    print("The square is", calculate_square(number))

# Function to calculate square
def calculate_square(number):
    return number * number

# Run the program
main()
