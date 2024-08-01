recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    
    ingredients = []
    print("Enter ingredients separated by commas (type 'done' when finished):")
    ingredients_input = input()
    if ingredients_input.lower() != 'done':
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

if __name__ == "__main__":
    recipes_list = []
    ingredients_list = []
    
    n = int(input("How many recipes would you like to enter? "))
    for _ in range(n):
        recipe = take_recipe()
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        recipes_list.append(recipe)
    
    print("Recipes entered:")
    for recipe in recipes_list:
        print(f"Name: {recipe['name']}")
        print(f"Cooking Time: {recipe['cooking_time']} minutes")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f" - {ingredient}")  # Print each ingredient
        print()  # Add a blank line for better readability
    
    print("All ingredients:")
    ingredients_list.sort()  # Sort ingredients alphabetically
    for ingredient in ingredients_list:
        print(f"  - {ingredient}")
    
    # Determine the difficulty of each recipe
    for recipe in recipes_list:
        cooking_time = recipe['cooking_time']
        num_ingredients = len(recipe['ingredients'])
        
        if cooking_time < 10 and num_ingredients < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and num_ingredients >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and num_ingredients < 4:
            difficulty = "Intermediate"
        else:
            difficulty = "Hard"
        
        # Add difficulty to the recipe dictionary
        recipe['difficulty'] = difficulty
   
    # Sort recipes by name
    recipes_list.sort(key=lambda x: x['name'])

    # Print recipes with difficulty
    for recipe in recipes_list:
        print(f"Name: {recipe['name']}")
        print(f"Cooking Time: {recipe['cooking_time']} minutes")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"  - {ingredient}")
        print(f"Difficulty: {recipe['difficulty']}")
        print()  # Add a blank line for better readability

    print("Ingredients Available Across All Recipes")
    ingredients_list.sort()  # Sort ingredients alphabetically again
    for ingredient in ingredients_list:
        print(f"  - {ingredient}")  # Print each ingredient