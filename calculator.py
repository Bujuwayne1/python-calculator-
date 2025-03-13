<<<<<<< HEAD
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
=======
# Basic Calculator
>>>>>>> 6b0038ff75a53ff4bfe51d42bd10d4122304b7ba
