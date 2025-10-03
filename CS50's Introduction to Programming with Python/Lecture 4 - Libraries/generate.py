import random   # Importing the random library for randomness

# Randomly pick between two options (like tossing a coin)
coin = random.choice(["Heads", "Tails"])
print("Coin Toss Result:", coin)

# Generate a random integer between 1 and 10 (inclusive)
number = random.randint(1, 10)
print("Random Number:", number)

# Shuffle a list of names randomly
gassTheName = ["sazit", "Ehosanul", "Islam"]
random.shuffle(gassTheName)   # This changes the list order in place

# Print each name in the shuffled list
for i in gassTheName:
    print("Shuffled Name:", i)
