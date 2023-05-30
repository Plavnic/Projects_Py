price = float(input("Enter the purchase amount: "))
fed_tax = price * 0.05
state_tax = price * 0.25
general_tax = fed_tax + state_tax
total_price = general_tax + price
print("The purchase amount: ", price)
print("The federal tax: ", fed_tax)
print("The state tax: ", state_tax)
print("The general tax: ", general_tax)
print("Total amount: ", total_price)
