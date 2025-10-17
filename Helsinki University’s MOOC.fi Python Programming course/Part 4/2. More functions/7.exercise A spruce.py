def spruce(size):
    print("a spruce!")
    
    i = 1
    while i <= size:
        spaces = size - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
        i += 1
    
    print(" " * (size - 1) + "*")

spruce(3)
print()
spruce(5)