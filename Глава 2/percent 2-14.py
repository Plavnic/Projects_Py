p = float(input("Enter the amount deposited to the savings account: "))
r = float(input("Enter the annual interest rate "
                "charged to the account balance: "))
n = float(input("Enter the frequency of interest income accrual per year: "))
t = float(input("Enter for how many years you have a savings account: "))
r = r / 100
a = p * ((1 + r / n) ** (n * t))
print("The amount of money after ", t, "years is ", format(a, '.2f'))
