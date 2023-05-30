r = float(input("The length of the bed in meters: "))
e = float(input("The amount of space occupied by the end support in meters: "))
s = float(input("The amount of space between the vines in meters: "))
v = (r - (e * 2)) / s
print("The number of vines that will fit in the garden is ", v)
