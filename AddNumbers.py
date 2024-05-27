# refactored calc fx
def add_numbers():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 + num2
        print(result)
    except ValueError:
        print("Invalid input! Please enter a number.")


add_numbers()