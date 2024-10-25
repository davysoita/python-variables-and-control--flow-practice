# a Python program that takes two numbers and an operation (+, -, *, /) from the user;  Perform the operation and print the result.
def calculate():
    a = int(input("Enter first number a"))
    b = int(input("Enter second number b"))
    operator = input("Entet the operator : ")
    output = 0
    if operator == "+":
        output = a+b
        return output
    elif operator == "-":
        output = a - b
        return output
    elif operator == "*":
        output = a * b
        return output
    elif operator == "/":
        output = a / b
        return output
print(calculate())