# Here is a more advanced calculator that you can practice with.

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not real.")
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def print_instructions():
    print("Advanced Calculator")
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Exit")

def calculator():
    print_instructions()

    while True:
        choice = input("Enter the operation number (1-10): ")

        if choice == '10':
            print("Exiting the calculator.")
            break

        if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print("Invalid choice. Please try again.")
            continue

        try:
            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            elif choice in ('6', '7', '8', '9'):
                num = float(input("Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            print("Result: {} + {} = {}".format(num1, num2, add(num1, num2)))
        elif choice == '2':
            print("Result: {} - {} = {}".format(num1, num2, subtract(num1, num2)))
        elif choice == '3':
            print("Result: {} * {} = {}".format(num1, num2, multiply(num1, num2)))
        elif choice == '4':
            try:
                print("Result: {} / {} = {}".format(num1, num2, divide(num1, num2)))
            except ValueError as e:
                print("Error:", e)
        elif choice == '5':
            print("Result: {} ^ {} = {}".format(num1, num2, exponentiate(num1, num2)))
        elif choice == '6':
            try:
                print("Result: √{} = {}".format(num, square_root(num)))
            except ValueError as e:
                print("Error:", e)
        elif choice == '7':
            print("Result: sin({}) = {}".format(num, sine(num)))
        elif choice == '8':
            print("Result: cos({}) = {}".format(num, cosine(num)))
        elif choice == '9':
            print("Result: tan({}) = {}".format(num, tangent(num)))

if __name__ == "__main__":
    calculator()


