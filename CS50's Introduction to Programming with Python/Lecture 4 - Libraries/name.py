import sys   # sys is needed to work with command-line arguments

# Check the number of arguments passed
if len(sys.argv) < 2:
    print("Too few arguments")   # No name given
elif len(sys.argv) > 2:
    print("Too many arguments")  # More than one name given
else:
    # Print the name provided as the second argument (sys.argv[0] is the file name itself)
    print("Hello, my name is", sys.argv[1])
