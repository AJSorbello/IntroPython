def get_valid_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= 120:
                return age
            else:
                print("Invalid input. Please enter an age between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

age = get_valid_age("Enter your age: ")
print("Age between 18 and 35: " + str(18 < age < 35))