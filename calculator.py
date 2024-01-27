def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    if b == 0:
        return "error!"
    else:
        return a/b

def square(a,b):
    b=a
    return a*b



print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Multiplication // just for 1. variable")

calculation = int(input("choose:"))

a = float(input("1. variable:"))
b = float(input("2. variable::"))


def multiply(a,b):
    return a*b


if calculation==1:
    print (sum(a,b))

elif calculation==2:
    print(sub(a,b))

elif calculation==3:
    print(div(a,b))

elif calculation==4:
    print(multiply(a,b))

elif calculation==5:
    print(square(a,b))