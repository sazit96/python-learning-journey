attempts = 0;
while True: 
    pin = int(input("PIN: "))
    attempts += 1
    if(pin != 4321):
        print("Wrong")
    elif(attempts == 1):
        print("Correct! It only took you one single attempt!")
        break
    else:
         print(f"Correct! It took you {attempts} attempts")
         break