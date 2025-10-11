limit = int(input("Limit: "))
num = 0
Sum = 0
calculation = ""

while Sum < limit:
    num += 1
    Sum += num
    calculation += str(num)
    if Sum < limit:
        calculation += " + "

print(f"The consecutive sum: {calculation} = {Sum}")
