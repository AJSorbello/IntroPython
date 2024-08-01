def get_valid_name(prompt):
	while True:
		name = input(prompt)
		if name.isalpha():
			return name.capitalize()
		else:
			print("Invalid input. Please enter a valid name containing only letters.")

first_name = get_valid_name("Enter your first name: ")
last_name = get_valid_name("Enter your last name: ")
print("Your name is", first_name, last_name)

