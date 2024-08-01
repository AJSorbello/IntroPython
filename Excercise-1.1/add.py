def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an number.")

a = get_integer("Enter a number: ")
b = get_integer("Enter a number: ")
c = a + b
print(f"The sum is: {c}")