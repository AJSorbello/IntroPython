# list_heroes.py

# Step 1: Read the data from Superheroes.txt
with open('Superheroes.txt', 'r') as file:
    superheroes = file.readlines()

# Step 2: Parse the data
superheroes_list = []
for line in superheroes:
    name, year = line.split(', ')
    year = year.strip()  # Remove any extra whitespace or newline characters
    superheroes_list.append((name, int(year)))

# Step 3: Sort the superheroes by year of first appearance
superheroes_list.sort(key=lambda x: x[1])

# Step 4: Print the sorted superheroes
for hero in superheroes_list:
    print(f"Superhero: {hero[0]}")
    print(f"Year of First Appearance: {hero[1]}")
    print()  # Print a newline for better readability
