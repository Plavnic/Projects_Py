print("Choose two colors to mix from red, yellow, blue")
color1 = input("Choose your first color: ")
color2 = input("Choose your second color: ")
colorsum = color1 + color2
if colorsum == "redblue" or colorsum == "bluered":
    print("You get a purple color! ")
elif colorsum == "redyellow" or colorsum == "yellowred":
    print("You get an orange color!")
elif colorsum == "blueyellow" or colorsum == "yellowblue":
    print("You get a green color!")
else:
    print("Error!")
