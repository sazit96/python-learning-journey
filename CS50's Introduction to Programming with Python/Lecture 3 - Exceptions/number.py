# -----------------------------
# Example 1: One-time try/except
# -----------------------------
# This way handles ValueError (non-integer input)
# try:
#     x = int(input("What is x? "))
#     # print(f"x is {x}")
# except:
#     print("X is not an integer")
# # Else only runs if no error occurs
# else:
#     print(f"x is {x}")


# -----------------------------
# Example 2: Reprompting until valid input
# -----------------------------
while True: 
    try:
        # Try to read input as integer
        x = int(input("What is x? "))
    except ValueError:
        # If user types non-integer, show message
        print("X is not an integer")
    else:
        # If conversion succeeded, exit loop
        break

# Print the valid integer entered by user
print(f"x is {x}")
