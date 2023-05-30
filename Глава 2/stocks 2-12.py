STOCKS = 2000
COMISSION = 0.03
BUY_PRICE = 40
SELL_PRICE = 42.75
price_total = STOCKS * BUY_PRICE
buy_comission = price_total * COMISSION
sell_total = STOCKS * SELL_PRICE
sell_comission = sell_total * COMISSION
profit = sell_total - (buy_comission + sell_comission + price_total)
print("The amount of money paid for the shares: ",
      format(price_total, '.2f'), "$")
print("The amount of the broker's commission when buying shares: ",
      format(buy_comission, '.2f'), "$")
print("The amount of the sale of shares: ",
      format(sell_total, '.2f'), "$")
print("The amount of the broker's commission for the sale of shares: ",
      format(sell_comission, '.2f'), "$")
print("The amount after the sale of shares and "
      "after deducting all commissions."
      "If the amount is positive, then profit, negative - loss: ",
      format(profit, '.2f'), "$")
