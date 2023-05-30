print("In this instruction answer 'yes' or 'no'.")
print("Restar the computer and try to connect.")
print("Has the problem been solved?")
answer = str(input())
if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Restar the router and try to connect.")
    print("Has the problem been solved?")
    answer = str(input())
    if answer == "yes":
        print("Great!")
    elif answer == "no":
        print("Check if the cables between router",
              "and modem are connected correctly")
        print("Has the problem been solved?")
        answer = str(input())
        if answer == "yes":
            print("Great!")
        elif answer == "no":
            print("Move the router to the new place")
            print("Has the problem been solved?")
            answer = str(input())
            if answer == "yes":
                print("Great!")
            elif answer == "no":
                print("Take a new router.")
            else:
                print("Choose the correct answer!")
        else:
            print("Choose the correct answer!")
    else:
        print("Choose the correct answer!")
else:
    print("Choose the correct answer!")
