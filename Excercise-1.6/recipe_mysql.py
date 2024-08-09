import mysql.connector

def main():
    # Establish the connection to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password',
        database='task_database'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create the Recipes table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recipes (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            ingredients VARCHAR(255),
            cooking_time INT,
            difficulty VARCHAR(20)
        )
    """)

    # Call the main menu function
    main_menu(conn, cursor)

    # The commit and connection closure are handled in main_menu(), so no need to do it here.

    print("Database and table setup complete.")

# Function to create a new recipe
def create_recipe(conn, cursor):
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(", ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    
    # Calculate difficulty based on cooking time and the number of ingredients
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert ingredients list to a comma-separated string
    ingredients_str = ", ".join(ingredients)
    
    cursor.execute("""
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    """, (name, ingredients_str, cooking_time, difficulty))
    
    conn.commit()
    print("Recipe added successfully!")

# Function to search for a recipe by ingredient
def search_recipe(conn, cursor):
    # Fetch all unique ingredients from the database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    # Build a list of all ingredients
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(", ")
        all_ingredients.update(ingredients)
    
    all_ingredients = list(all_ingredients)
    
    # Display available ingredients to the user
    print("Available ingredients:")
    for idx, ingredient in enumerate(all_ingredients, start=1):
        print(f"{idx}. {ingredient}")
    
    # Allow the user to select an ingredient
    choice = int(input("Enter the number of the ingredient you want to search for: "))
    search_ingredient = all_ingredients[choice - 1]
    
    # Search for recipes containing the selected ingredient
    cursor.execute("""
        SELECT * FROM Recipes WHERE ingredients LIKE %s
    """, ('%' + search_ingredient + '%',))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No recipes found with that ingredient.")

# Function to input difficulty
def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    return difficulty

# Function to update an existing recipe
def update_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    print("Available recipes:")
    for recipe in recipes:
        print(recipe)
    
    # Allow the user to select a recipe by ID
    recipe_id = int(input("Enter the ID of the recipe you want to update: "))
    
    # Allow the user to select a column to update
    print("Which column would you like to update?")
    print("1. Name")
    print("2. Cooking time")
    print("3. Ingredients")
    column_choice = input("Enter the number of the column to update: ")
    
    # Update the selected column
    if column_choice == "1":
        new_name = input("Enter the new recipe name: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_name, recipe_id))
    
    elif column_choice == "2":
        new_cooking_time = int(input("Enter the new cooking time in minutes: "))
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_cooking_time, recipe_id))
        
        # Recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients = ingredients_str.split(", ")
        new_difficulty = calculate_difficulty(new_cooking_time, ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))
    
    elif column_choice == "3":
        new_ingredients = input("Enter the new ingredients (comma-separated): ").split(", ")
        ingredients_str = ", ".join(new_ingredients)
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (ingredients_str, recipe_id))
        
        # Recalculate difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        new_difficulty = calculate_difficulty(cooking_time, new_ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))
    
    conn.commit()
    print("Recipe updated successfully!")

# Function to delete a recipe
def delete_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    print("Available recipes:")
    for recipe in recipes:
        print(recipe)
    
    # Allow the user to select a recipe by ID
    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))
    
    # Delete the selected recipe
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

# The main menu function
def main_menu(conn, cursor):
    while True:
        print("\nRecipe Database Menu")
        print("1. Add a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    # Commit any remaining changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Database connection closed.")

# Run the main function
if __name__ == "__main__":
    main()
