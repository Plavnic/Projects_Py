price = float(input('Enter the food price: '))
tax = price * 0.07
tips = price * 0.18
total = tax + tips + price
print("The food price: ", format(price, '.2f'), "$")
print("The taxes: ", format(tax, '.2f'), "$")
print("The tips: ", format(tips, '.2f'), "$")
print("The total price: ", format(total, '.2f'), "$")
