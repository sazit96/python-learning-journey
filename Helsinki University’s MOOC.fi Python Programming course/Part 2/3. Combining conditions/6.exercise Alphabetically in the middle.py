a = input ("1st letter: ")
b = input ("2nd letter: ")
c = input ("3rd letter: ")
if(a <= b <= c) or (c <= b <= a): middle = b
elif (b <= a <= c) or (c <= a <= b): middle = a
else: middle = c
print(f"The letter in the middle is {middle}");

