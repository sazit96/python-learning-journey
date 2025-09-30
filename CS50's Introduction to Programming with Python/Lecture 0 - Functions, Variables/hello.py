Basic print (commented)
print("hello, world")

Input name, remove spaces, and format
name = input("What's your name? ").strip().capitalize().title()

Step-by-step formatting (for practice)
name = name.strip()            # Remove spaces
name = name.capitalize()       # Capitalize first letter
name = name.title()            # Capitalize each word
name = name.title().strip().capitalize()  # Extra chaining

Different print styles (commented)
print("hello >", name)
print("hello ", end="")
print(name)

Print with escaped quotes
print("hello \"friend\"")

# Final greeting
print(f"Hello, {name}")
