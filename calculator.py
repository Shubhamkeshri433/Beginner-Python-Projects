def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Cannot divide by 0")
    return a / b

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("/n Choose an operator:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

operator = input("Enter operator: ")

if operator == "+":
    print("Result: ", add(number1, number2))

elif operator == "-":
    print("Result: ", sub(number1, number1))

elif operator == "*":
    print("Result: ", multi(number1, number2))

elif operator == "/":
    print("Resuly: ", div(number1, number2))

else:
    print("Invalid Operator")