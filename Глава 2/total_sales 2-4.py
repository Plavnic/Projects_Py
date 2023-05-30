price_1 = float(input("Введите стоймость 1 товара: "))
price_2 = float(input("Введите стоймость 2 товара: "))
price_3 = float(input("Введите стоймость 3 товара: "))
price_4 = float(input("Введите стоймость 4 товара: "))
price_5 = float(input("Введите стоймость 5 товара: "))
total_price = (price_1 + price_2
               + price_3 + price_4 + price_5)
comission = total_price * 0.07
end_price = total_price - comission
print("Общая стоймость без вычета комиссии: ",
      total_price)
print("Сумма комиссии: ", comission)
print("Общая стоймость с учетом вычета комиссии",
      end_price)
