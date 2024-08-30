# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

# Main calculator function
def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter the operation (1/2/3/4): ")

    # Perform the calculation based on user choice
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation choice"

    # Display the result
    print("Result:", result)

# Run the calculator
calculator()