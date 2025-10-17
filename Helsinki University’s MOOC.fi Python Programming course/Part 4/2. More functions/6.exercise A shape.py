def triangle(n, s1):
    s = ""
    while n > 0:
        s += s1
        print(s)
        n -= 1

def square(n1, n2, s):
    while n2 > 0:
        print(n1 * s)
        n2 -= 1

def shape (n1 , s1, n2, s2):
    triangle(n1,s1)
    square (n1,n2,s2)


shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
