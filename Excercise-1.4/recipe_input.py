import pickle

def calc_difficulty(cooking_time, ingredients):
    """
    Calculate the difficulty of the recipe based on cooking time and the number of ingredients.
    """
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    return difficulty

def take_recipe():
    """
    Take the recipe details from the user and return a dictionary containing the recipe attributes.
    """
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (separated by commas): ").split(", ")
    
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe

filename = input("Enter the filename where you'd like to store your recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print(f"File '{filename}' loaded successfully.")
        if 'recipes_list' not in data or 'all_ingredients' not in data:
            raise KeyError("Missing expected keys in the loaded data.")
except (FileNotFoundError, KeyError):
    print("File not found or data structure incorrect. Creating a new file.")
    data = {'recipes_list': [], 'all_ingredients': []}
except Exception as e:
    print(f"An error occurred: {e}. Creating a new file.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num_recipes = int(input("How many recipes would you like to enter? "))

for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)
    
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

with open(filename, 'wb') as file:
    pickle.dump(data, file)
    print(f"Data saved successfully to '{filename}'.")

print("Recipes and ingredients saved successfully!")
