class Recipe:
    all_ingredients = set()
    
    def __init__(self, name, ingredients=None, cooking_time=0):
        self._name = name
        self._ingredients = ingredients if ingredients is not None else []
        self._cooking_time = cooking_time
        self._difficulty = None
        self.calculate_difficulty()
        self.update_all_ingredients()
    
    # Getter and Setter for name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    # Getter and Setter for cooking_time
    @property
    def cooking_time(self):
        return self._cooking_time
    
    @cooking_time.setter
    def cooking_time(self, value):
        self._cooking_time = value
        self.calculate_difficulty()

    # Method to add ingredients
    def add_ingredients(self, *args):
        self._ingredients.extend(args)
        self.update_all_ingredients()
        self.calculate_difficulty()
    
    # Getter for ingredients
    @property
    def ingredients(self):
        return self._ingredients
    
    # Method to calculate difficulty
    def calculate_difficulty(self):
        if self._cooking_time < 10:
            if len(self._ingredients) < 4:
                self._difficulty = 'Easy'
            else:
                self._difficulty = 'Medium'
        else:
            if len(self._ingredients) < 4:
                self._difficulty = 'Intermediate'
            else:
                self._difficulty = 'Hard'
    
    # Getter for difficulty
    @property
    def difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty
    
    # Method to search for an ingredient
    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients
    
    # Method to update all ingredients
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self._ingredients)
    
    # String representation of the Recipe object
    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}")
    
    # Method to search for recipes containing a specific ingredient
    @staticmethod
    def recipe_search(data, search_term):
        for recipe in data:
            contains_ingredient = recipe.search_ingredient(search_term)
            print(f"{recipe.name}: {contains_ingredient}")

# Create the 'tea' recipe object
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5

# Create the 'coffee' recipe object
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5

# Create the 'cake' recipe object
cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50

# Create the 'banana smoothie' recipe object
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5

# Add all recipes to a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Display the string representation of each recipe
for recipe in recipes_list:
    print(recipe)
    print()

# Example usage of the recipe_search method
print("Search results for 'Sugar':")
Recipe.recipe_search(recipes_list, "Sugar")
