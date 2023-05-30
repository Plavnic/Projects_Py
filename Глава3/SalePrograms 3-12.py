sale = 0
total = 0
price = 99

programs = int(input("Input the amount of bought programs: "))
if programs >= 10 and programs <= 19:
    sale = price * programs * 0.1
    total = price * programs - sale
if programs >= 20 and programs <= 49:
    sale = price * programs * 0.2
    total = price * programs - sale
if programs >= 50 and programs <= 99:
    sale = price * programs * 0.3
    total = price * programs - sale
if programs >= 100:
    sale = price * programs * 0.4
    total = price * programs - sale

print("The sale amount is", format(sale, '.2f'), "$")
print("Total price with sale for your order is:", format(total, '.2f'), "$")
