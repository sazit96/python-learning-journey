# ----------------------------
# Print a column of "#"
# ----------------------------
def main():
    coloum(3)   # print 3 rows (vertical)

def coloum(height):
    print("#\n" * height)   # "\n" makes new line after each "#"

main()


# ----------------------------
# Print a single row of "*"
# ----------------------------
def main():
    print_row(5)  # print 5 stars in a row

def print_row(width):
    print("* " * width)   # repeat "* " width times

main()


# ----------------------------
# Print a square using nested loops
# ----------------------------
def main():
    print_square(5)  # print a 5x5 square

# Version 1: using nested loops
def print_square(size):
    for i in range(size):         # loop over rows
        for j in range(size):     # loop over columns
            print("# ", end="")   # print "#" without newline
        print()                   # move to next row

# Version 2: shorter way using string multiplication
def print_square(size):
    for i in range(size):         # loop over rows
        print("# " * size)        # each row is "# " repeated size times

main()
