BunsInPackage = 8
SausagesInPack = 10
print("Input the amount of people on picnic and how much "
      "hotdogs each of them will eat ")
people = int(input("Input the amount of people: "))
hotdogs = int(input("Input the amount of hotdogs for 1 person: "))
TotalHotdogs = people * hotdogs
TotalBunsPackage = TotalHotdogs // BunsInPackage

if TotalHotdogs % BunsInPackage != 0:
    TotalBunsPackage += 1
    LeftBuns = TotalBunsPackage * BunsInPackage - TotalHotdogs
else:
    TotalBunsPackage = TotalBunsPackage
    LeftBuns = 0


TotalSausagesPack = TotalHotdogs // SausagesInPack

if TotalHotdogs % SausagesInPack != 0:
    TotalSausagesPack += 1
    LeftSausages = TotalSausagesPack * SausagesInPack - TotalHotdogs
else:
    TotalSausagesPack = TotalSausagesPack
    LeftSausages = 0


print("The minimum required number of packages with sausages is",
      TotalSausagesPack)
print("The minimum required number of packages with buns is",
      TotalBunsPackage)
print("The amount of left sausages is", LeftSausages)
print("The amount of left buns is", LeftBuns)
