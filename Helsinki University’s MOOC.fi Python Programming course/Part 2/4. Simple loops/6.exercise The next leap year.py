year = int(input("Year: "))
main_year = year
while True: 
    year += 1;
    if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print(f"The next leap year after {main_year} is {year}")
        break