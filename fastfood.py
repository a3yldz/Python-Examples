print("1. Hamburger")
print("2. Pizza")
print("3. Sandwich")
choose=input("Choose a fast food type ")


Hamburger=50
Pizza=48
Sandwich=39
Total=0
Menu=10

if choose=='H'or choose=='h':
    print(Hamburger, "TL")
    Total=Hamburger
elif choose=='P' or choose=='p':
    print(Pizza , "TL")
    Total=Pizza
elif choose=='S' or choose=='s':
    print(Sandwich, "TL")
    Total=Sandwich


menu=input("Do you want a menu ")
if menu=='Y'or menu=='y':
    print(Total+Menu, "TL")
elif menu=='N' or menu=='n':
    print("Just product:", Total)