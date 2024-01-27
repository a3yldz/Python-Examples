#Basic atm example. There is not OOP. You can verify, welcome, withdraw and deposit operations.

balance=1000
uname="Atakan"
upass= 123456
def verify(name, password):
    if name ==uname and upass==password:
          print("Verify")
    else:
        print("Fail")
        return False
def welcome(name):
    print("Welcome", name)
    print("You have", balance, "TL")
def withdraw(money):
    balance=1000
    current= balance-money
    if current>=0:
        print("Withdrawing...")
        print("Succsessfull")
        print("You have", current, "TL")
    else:
         print("You have", balance, "TL. You cant withdraw money")
def deposit(money):
        current= balance+money
        print("Deposit...")
        print("Succsessfull")
        print("You have", current, "TL")

verify("Atakan", 123456)
welcome(uname)
withdraw(200)
deposit(1000)