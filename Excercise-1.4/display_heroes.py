def display(file):
    heroes = []
    for line in file:
        # Removing newline characters
        line = line.rstrip("\n")

        # Split the line into hero name and first appearance year
        parts = line.split(", ")
        hero_name = parts[0]
        first_appearance = parts[1]

        # Append the hero information to the list
        heroes.append([hero_name, first_appearance])

    # Sort the heroes by the year of first appearance
    heroes.sort(key=lambda hero: hero[1])

    # Print the sorted heroes
    for hero in heroes:
        print("--------------------------------------")
        print("Superhero: " + hero[0])
        print("First year of appearance: " + hero[1])

# Main block to handle file operations and error handling
filename = input("Enter the filename where you've stored your superheroes: ")
try:
    file = open(filename, 'r')
    display(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    file.close()
finally:
    print("Goodbye!")
