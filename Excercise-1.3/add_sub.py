# add_sub.py

# Get user inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+ or -): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
    print("Result: " + str(num1 + num2))

elif operation == "-":
    result = num1 - num2
    print("Result: " + str(num1 - num2))

else:
    print("Invalid operation. Please enter either + or -.")