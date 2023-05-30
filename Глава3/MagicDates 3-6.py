day = int(input("Input the day: "))
mounth = int(input("Input the mounth: "))
year = int(input("Input the last 2 numbers of the year: "))
magic = day * mounth
if magic == year:
    print("This is a magic date!")
else:
    print("This is not a magic date :(")
