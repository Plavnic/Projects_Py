length1 = float(input("Input the length of the first rectangle in 'cm' : "))
width1 = float(input("Input the width of the first rectangle in 'cm' : "))
length2 = float(input("Input the length of the second rectangle in 'cm' : "))
width2 = float(input("Input the width of the second rectangle in 'cm' : "))
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print("Area of the first rectangle is bigger than area of the second")
elif area1 < area2:
    print("Area of the second rectangle is bigger than area of the first")
elif area1 == area2:
    print("Areas of two rectangles are equel")
