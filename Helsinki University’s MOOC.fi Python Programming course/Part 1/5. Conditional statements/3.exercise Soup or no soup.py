name = input("Please tell me your name:")
if(name == "Jerry"): print("Next please!")
else:
    portions = float(input("How many portions of soup?"))
    print(f"The total cost is {portions * 5.90}")
    print("Next please!")