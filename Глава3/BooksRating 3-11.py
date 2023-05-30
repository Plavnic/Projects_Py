books = int(input("Input the amount of the books bought this month: "))
if books <= 1:
    print("You've earned 0 points!")
elif books <= 3:
    print("You've earned 5 points!")
elif books <= 5:
    print("You've earned 15 points!")
elif books <= 7:
    print("You've earned 30 points!")
elif books >= 8:
    print("You've earned 60 points!")
