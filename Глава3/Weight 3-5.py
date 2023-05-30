mass = float(input("Input your mass in kg: "))
weight = mass * 9.8
if weight > 500:
    print("Your weight is", format(weight, '.2f'), "newtons.",
          "Your body is too heavy!")
elif weight < 100:
    print("Your weight is", format(weight, '.2f'), "newtons.",
          "Your body is too light!")
else:
    print("Your weight is", format(weight, '.2f'), "newtons.",
          "Your body is great!")
