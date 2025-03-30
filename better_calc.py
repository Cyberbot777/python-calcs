# Building a better calculator
# This script performs basic arithmetic operations on two numbers with error handling.

# Get user input for the first number
try:
    num1 = float(input("Enter first number: "))
except ValueError:
    print("Error: Please enter a valid number for the first input.")
    exit()

# Get the operator
operator = input("Enter operator (+, -, *, /): ")

# Validate the operator
valid_operators = ['+', '-', '*', '/']
if operator not in valid_operators:
    print("Error: Invalid operator. Please use +, -, *, or /.")
    exit()

# Get user input for the second number
try:
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter a valid number for the second input.")
    exit()

# Perform the calculation with error handling for division by zero
try:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    # Display the full equation
    print(f"{num1} {operator} {num2} = {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Future improvement: Add support for more operations like exponentiation (^) or modulus (%)