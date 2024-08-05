def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    print("Select the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    user = input("Enter your option: ")
    
    if user == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif user == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif user == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif user == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid option. Please select a valid operation.")
        
calculator()
