gift = int(input("Value of gift: "))

if gift < 5000:
    print("No tax!")
elif gift < 25000:
    tax = 100 + (gift - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")
elif gift < 55000:
    tax = 1700 + (gift - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")
elif gift < 200000:
    tax = 4700 + (gift - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif gift < 1000000:
    tax = 22100 + (gift - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
else:
    tax = 142100 + (gift - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")
