import pickle

def display_recipe(recipe):
    """
    Display the attributes of a recipe.
    """
    print(f"Recipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print('')

def search_ingredient(data):
    """
    Search for recipes containing a specific ingredient.
    """
    ingredients = data['all_ingredients']
    print("Available Ingredients:")
    for index, ingredient in enumerate(ingredients):
        print(f"{index}. {ingredient}")

    try:
        ingredient_index = int(input("Enter the number corresponding to the ingredient you want to search for: "))
        ingredient_searched = ingredients[ingredient_index]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number corresponding to the ingredient.")
        return

    print(f"\nRecipes containing '{ingredient_searched}':")
    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)

filename = input("Enter the filename where your recipes are stored: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print(f"File '{filename}' loaded successfully.")
except FileNotFoundError:
    print("File not found. Please make sure the file exists.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    search_ingredient(data)
finally:
    print("Search completed.")
