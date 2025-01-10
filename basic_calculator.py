def calculator():
    print("Welcome to the Basic Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the user's choice
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Get numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the chosen operation
    if choice == "1":
        print(f"The result is: {num1 + num2}")
    elif choice == "2":
        print(f"The result is: {num1 - num2}")
    elif choice == "3":
        print(f"The result is: {num1 * num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select a valid operation.")

# Run the calculator
calculator()
