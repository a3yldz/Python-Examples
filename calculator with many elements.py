def addition(*args):
    return sum(args)

def subtraction(x, *args):
    return x - sum(args)

def multiplication(*args):
    result = 1
    for num in args:
        result *= num
    return result

def division(x, *args):
    result = x
    for num in args:
        if num == 0:
            return "Division by zero error!"
        else:
            result /= num
    return result

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

numbers = [float(x) for x in input("Enter numbers (separated by commas): ").split(',')]

if choice == '1':
    print("Addition Result:", addition(*numbers))

elif choice == '2':
    print("Subtraction Result:", subtraction(*numbers))

elif choice == '3':
    print("Multiplication Result:", multiplication(*numbers))

elif choice == '4':
    print("Division Result:", division(*numbers))

else:
    print("Invalid input")
