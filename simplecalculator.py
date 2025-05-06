# simple_calculator.py
import math

while True:
    print("\nWelcome to Simple Calculator")
    print("Choose the operation you want to do:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modular Division")
    print("6. Square Root")
    print("7. Exponentiation")
    print("8. Exit")

    try:
        choice = int(input("\nPlease enter your choice (1-8): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is = {num1 + num2}")

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The subtraction of {num1} and {num2} is = {num1 - num2}")

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The multiplication of {num1} and {num2} is = {num1 * num2}")

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"The division of {num1} and {num2} is = {num1 / num2}")
        else:
            print("Cannot divide by zero.")

    elif choice == 5:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"The modular division of {num1} and {num2} is = {num1 % num2}")
        else:
            print("Cannot perform modulo with zero.")

    elif choice == 6:
        num1 = float(input("Enter your number: "))
        if num1 >= 0:
            print(f"The square root of {num1} is = {math.sqrt(num1)}")
        else:
            print("Cannot calculate square root of a negative number.")

    elif choice == 7:
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent number: "))
        print(f"{num1} raised to the power {num2} is = {math.pow(num1, num2)}")

    elif choice == 8:
        print("You chose to exit. Bye!")
        break

    else:
        print("Invalid input. Please choose a number from 1 to 8.")
