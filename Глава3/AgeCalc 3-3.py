age = int(input("Enter an age of a person: "))
if age <= 1:
    print("It's a baby")
elif age > 1 and age < 13:
    print("It's a child")
elif age >= 13 and age < 20:
    print("It's a teenager")
elif age >= 20:
    print("It's an adult")
