while True:
    num = int(input("Please type in a number: "))
    
    if num <= 0:
        print("Thanks and bye!")
        break
    
    i = 1 
    result = 1
    while i <= num: 
        result *= i
        i += 1
    
    print(f"The factorial of the number {num} is {result}")