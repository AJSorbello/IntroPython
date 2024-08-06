class ShoppingList(object):
    def __init__(self, list_name):
        # (Initialize Method) initializes the ShoppingList with a name and an empty list for items.
        self.list_name = list_name
        self.shopping_list = []
        
    def add_item(self, item):
        # (Add Method) an item to the shopping list if it is not already present.
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            print(f"{item} is already in the shopping list.")
            
    def remove_item(self, item):
        # (Remove Method) removes an item from the shopping list if it exists.
        if item in self.shopping_list:
            self.shopping_list.remove(item)
        else:
            print(f"{item} is not in the shopping list.")

    def view_list(self):
        # (View Method) View the contents of the shopping list.
        if self.shopping_list:
            print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
            for item in self.shopping_list:
                print(f"- {item}")
        else:
            print(f"The shopping list '{self.list_name}' is empty.")


    def merge_lists(self, obj):    
        # Creating a name for our new, merged shopping list
        merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

        # Creating an empty ShoppingList object
        merged_lists_obj = ShoppingList(merged_lists_name)

        # Adding the first shopping list's items to our new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        # Adding the second shopping list's items to our new list -
        # we're doing this so that there won't be any repeated items
        # in the final list, if both source lists contain common
        # items between each other
        for item in obj.shopping_list:
            if item not in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)

        # Returning our new, merged object
        return merged_lists_obj

# Create objects of the ShoppingList class
pet_store_list = ShoppingList("Pet Store Shopping List")
grocery_store_list = ShoppingList("Grocery Store List")

# Add items to the pet store shopping list
for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

# Add items to the grocery store shopping list
for item in ['fruits', 'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

# Merge the lists
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# View the merged list
merged_list.view_list()

# Add items to the shopping list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item from the shopping list
pet_store_list.remove_item("flea collars")

# Try adding an item that is already in the list
pet_store_list.add_item("frisbee")

# Display the entire shopping list
pet_store_list.view_list()
