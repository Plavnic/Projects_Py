girls = int(input("Number of female students: "))
boys = int(input("Number of male students: "))
all = girls + boys
girls_percent = (girls / all) * 100
boys_percent = (boys / all) * 100
print("The percent of female students is: ",
      format(girls_percent, '.2f'), "%")
print("The percent of male students is: ",
      format(boys_percent, '.2f'), "%")
