import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL credentials
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
hostname = os.getenv("HOSTNAME")
database_name = os.getenv("DATABASE_NAME")

# Create the engine object
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{hostname}/{database_name}"
)

# Set up the base class
Base = declarative_base()


# Define the Recipe model
class Recipe(Base):
    """
    A class used to represent a Recipe.

    Attributes:
    ----------
    id : int
        The unique identifier for the recipe.
    name : str
        The name of the recipe.
    ingredients : str
        The ingredients of the recipe.
    cooking_time : int
        The cooking time in minutes.
    difficulty : str
        The difficulty level of the recipe.
    """

    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Recipe object.
        """
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"

    def __str__(self):
        """
        Returns a formatted string representation of the Recipe object.
        """
        return (
            f"\nRecipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}\n"
        )

    def calculate_difficulty(self):
        """
        Calculates and sets the difficulty level of the recipe based on the number of ingredients and cooking time.
        """
        ingredients_list = self.return_ingredients_as_list()
        num_ingredients = len(ingredients_list)
        if num_ingredients <= 4:
            self.difficulty = "Easy"
        elif num_ingredients > 4 and num_ingredients <= 5:
            if self.cooking_time < 20:
                self.difficulty = "Medium"
            else:
                self.difficulty = "Intermediate"
        else:
            if self.cooking_time < 30:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        """
        Returns the ingredients as a list.
        """
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")


def create_recipe(session):
    """
    Collects recipe details from the user and adds a new recipe to the database.
    """
    name = input("Enter the recipe name: ")
    while len(name) > 50:
        print("Invalid input. Please enter a name with 50 characters or fewer.")
        name = input("Enter the recipe name: ")

    ingredients = []
    num_ingredients = input("How many ingredients would you like to enter? ")
    while not num_ingredients.isnumeric():
        print("Invalid input. Please enter a number.")
        num_ingredients = input("How many ingredients would you like to enter? ")

    for i in range(int(num_ingredients)):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)

    ingredients_str = ", ".join(ingredients)

    cooking_time = input("Enter the cooking time in minutes: ")
    while not cooking_time.isnumeric():
        print("Invalid input. Please enter a number.")
        cooking_time = input("Enter the cooking time in minutes: ")

    # Create a new Recipe object
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=int(cooking_time),
        difficulty="",
    )

    # Calculate and assign difficulty
    recipe_entry.calculate_difficulty()

    # Add the new recipe to the database
    session.add(recipe_entry)
    session.commit()

    print("Recipe added successfully!")


def view_all_recipes(session):
    """
    Retrieves and displays all recipes from the database.
    """
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found in the database.")
        return None

    for recipe in recipes:
        print(recipe)


def search_by_ingredients(session):
    """
    Searches for recipes based on selected ingredients.
    """
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return None

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    selected_numbers = input(
        "Enter the numbers corresponding to the ingredients you'd like to search for, separated by spaces: "
    ).split()
    if not all(
        num.isnumeric() and 1 <= int(num) <= len(all_ingredients)
        for num in selected_numbers
    ):
        print("Invalid input. Exiting search.")
        return None

    search_ingredients = [all_ingredients[int(num) - 1] for num in selected_numbers]

    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    recipes = session.query(Recipe).filter(*conditions).all()
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")


def edit_recipe(session):
    """
    Edits an existing recipe in the database.
    """
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return None

    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")

    selected_id = input("Enter the id of the recipe you'd like to edit: ")
    if (
        not selected_id.isnumeric()
        or not session.query(Recipe).filter_by(id=int(selected_id)).first()
    ):
        print("Invalid id. Exiting edit.")
        return None

    recipe_to_edit = session.query(Recipe).filter_by(id=int(selected_id)).first()
    print(f"Editing Recipe: {recipe_to_edit.name}")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")

    option = input(
        "Enter the number corresponding to the attribute you'd like to edit: "
    )

    if option == "1":
        new_name = input("Enter the new recipe name: ")
        while len(new_name) > 50:
            print("Invalid input. Please enter a name with 50 characters or fewer.")
            new_name = input("Enter the new recipe name: ")
        recipe_to_edit.name = new_name

    elif option == "2":
        ingredients = []
        num_ingredients = input("How many ingredients would you like to enter? ")
        while not num_ingredients.isnumeric():
            print("Invalid input. Please enter a number.")
            num_ingredients = input("How many ingredients would you like to enter? ")

        for i in range(int(num_ingredients)):
            ingredient = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ingredient)

        ingredients_str = ", ".join(ingredients)
        recipe_to_edit.ingredients = ingredients_str

    elif option == "3":
        new_time = input("Enter the new cooking time in minutes: ")
        while not new_time.isnumeric():
            print("Invalid input. Please enter a number.")
            new_time = input("Enter the new cooking time in minutes: ")
        recipe_to_edit.cooking_time = int(new_time)

    else:
        print("Invalid option. Exiting edit.")
        return None

    # Recalculate difficulty after editing
    recipe_to_edit.calculate_difficulty()

    session.commit()
    print("Recipe updated successfully!")


def delete_recipe(session):
    """
    Deletes a recipe from the database.
    """
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return None

    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")

    selected_id = input("Enter the id of the recipe you'd like to delete: ")
    if (
        not selected_id.isnumeric()
        or not session.query(Recipe).filter_by(id=int(selected_id)).first()
    ):
        print("Invalid id. Exiting delete.")
        return None

    recipe_to_delete = session.query(Recipe).filter_by(id=int(selected_id)).first()

    confirm = input(
        f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): "
    ).lower()
    if confirm == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Delete operation canceled.")


def main_menu():
    """
    Displays the main menu and handles user input.
    """
    # Generate the session class and bind it to the engine
    Session = sessionmaker(bind=engine)

    # Initialize the session object within a context manager
    with Session() as session:
        while True:
            print("\n--- Recipe Manager ---")
            print("1. Create a new recipe")
            print("2. View all recipes")
            print("3. Search for recipes by ingredients")
            print("4. Edit a recipe")
            print("5. Delete a recipe")
            print("Type 'quit' to exit the application.")

            choice = input("Please choose an option: ").strip().lower()

            if choice == "1":
                create_recipe(session)
            elif choice == "2":
                view_all_recipes(session)
            elif choice == "3":
                search_by_ingredients(session)
            elif choice == "4":
                edit_recipe(session)
            elif choice == "5":
                delete_recipe(session)
            elif choice == "quit":
                print("Exiting the application. Goodbye!")
                break
            else:
                print(
                    "Invalid input. Please enter a number between 1-5 or 'quit' to exit."
                )


if __name__ == "__main__":
    # Create the table in the database
    Base.metadata.create_all(engine)

    # Run the main menu
    main_menu()
