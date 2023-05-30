Rub5 = 5
Rub10 = 10
Rub50 = 50
total = 100
print("Добро пожаловать в игру !")
print("Попробуй набрать 100 рублей монетками по 5, 10 и 50 копеек")
num1 = int(input("Введи сколько нужно монеток по 5: "))
num2 = int(input("Введи количество монеток по 10: "))
num3 = int(input("Введи количество монеток по 50: "))
money1 = num1 * Rub5
money2 = num2 * Rub10
money3 = num3 * Rub50
TotalMoney = money1 + money2 + money3
if TotalMoney == total:
    print("Ты молодец! У тебя получился 1 рубль!")
elif TotalMoney > total:
    sumRub = TotalMoney - total
    print("Ох, мы немного переборщили, на целых",
          sumRub, "копейки. Ну ничего! В следующий раз точно получится :)")
elif TotalMoney < total:
    sumRub = total - TotalMoney
    print("Ох, у нас небольшой недобор, на целых",
          sumRub, "копейки. Ну ничего! В следующий раз точно получится :)")
