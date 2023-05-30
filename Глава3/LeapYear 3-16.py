year = int(input("Input the year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("It's 29 days in February in", year, "year")
else:
    if year % 4 == 0:
        print("It's 29 days in February in", year, "year")
    else:
        print("It's 28 days in February in", year, "year")
