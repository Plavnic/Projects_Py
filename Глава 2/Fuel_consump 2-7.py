dist = float(input('Enter the traveled kilometers: '))
fuel = float(input('Enter the fuel consumption in liters: '))
consmp = dist / fuel
print('The consumption of the car is', format(consmp, ".2f"),
      'kilometers per 1 liter')
