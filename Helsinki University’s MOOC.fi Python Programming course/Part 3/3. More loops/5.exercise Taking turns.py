num = int(input("Please type in a number: "))

left = 1
right = num

while left <= right:
    print(left)
    if left < right:
        print(right)
    left += 1
    right -= 1