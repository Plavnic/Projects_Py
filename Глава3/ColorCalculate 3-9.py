Number = int(input("Please, input the number of the roulette pocket"
                   "between 0 and 36: "))
if Number < 0 or Number > 36:
    print('Error!')
elif Number == 0:
    print("This pocket is green.")
elif Number >= 1 and Number <= 10:
    if Number % 2 == 0:
        print("This pocket is black.")
    else:
        print("This pocket is red.")
elif Number >= 11 and Number <= 18:
    if Number % 2 == 0:
        print("This pocket is red.")
    else:
        print("This pocket is black.")
elif Number >= 19 and Number <= 28:
    if Number % 2 == 0:
        print("This pocket is black.")
    else:
        print("This pocket is red.")
elif Number >= 29 and Number <= 36:
    if Number % 2 == 0:
        print("This pocket is red.")
    else:
        print("This pocket is black.")
