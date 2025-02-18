def add(a, b):
    return a + b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))



def subtract(a, b):
    return a - b

10


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."


print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")


choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    print("The sum is:", add(a, b))
elif choice == '2':
    print("The difference is:", subtract(a, b))
elif choice == '3':
    print("The product is:", multiply(a, b))

else:
    print("Invalid input")