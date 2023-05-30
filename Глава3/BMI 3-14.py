weight = float(input("Input your weight in kilograms: "))
height = float(input("Input your height in meters: "))
bmi = weight / (height ** 2)
if bmi >= 18.5 and bmi <= 25:
    print("Your BMI is optimal!")
elif bmi <= 18.5:
    print("Your BMI is too low!")
elif bmi >= 25:
    print("Your BMI is too high!")
