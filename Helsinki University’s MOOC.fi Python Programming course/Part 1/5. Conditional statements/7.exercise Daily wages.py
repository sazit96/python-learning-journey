hour = float(input("Hourly wage: "))
work = float(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    print(f"Daily wages: {(hour * work) * 2:.1f} euros")
else:
    print(f"Daily wages: {hour * work:.1f} euros")
