weight = int(input("Input the weight of your package in gramms: "))
if weight <= 200:
    price = weight * 1.5
if weight > 200 and weight <= 600:
    price = weight * 3
if weight > 600 and weight <= 1000:
    price = weight * 4
if weight > 1000:
    price = weight * 4.75

print("The delivery cost is", format(price, '.2f'), "rubles")
