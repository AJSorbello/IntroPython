class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    # We'll throw in getter methods for age and name       
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # And setter methods as well
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # We'll also have a well-formatted string representation, too!
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

# We'll create a Cat class that inherits from the Animal class
class Cat(Animal):
    def __init__(self, age):
        super().__init__(age)

    # Introducing a new method where it speaks
    def speak(self):
        print("Meow")

    # Another neat string representation for cats
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

# We'll create a Dog class that inherits from the Animal class
class Dog(Animal):
    def __init__(self, age):
        super().__init__(age)

    # Introducing a new method where it speaks
    def speak(self):
        print("Woof!")

    # String representation for dogs
    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

# Creating instances of Cat and Dog
cat = Cat(3)
dog = Dog(6)

# Naming the pets
cat.set_name("Stripes")
dog.set_name("Bubbles")

# Printing the objects
print(cat)
print(dog)


class Human(Animal):
    # Making its own initialization method
    def __init__(self, name, age):
        super().__init__(age)

        # Setting a name, since humans must have names
        self.set_name(name)

        # Our new attribute for humans, 'friends'!
        self.friends = []

    # Adding another method to add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    # A method to display friends
    def show_friends(self):
        for friend in self.friends:
            print(friend)

    # Humans can speak sentences!
    def speak(self):
        print("Hello, my name's " + self.name + "!")

    # We'll modify the string representation to include friends as well.
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output
    
human = Human("Tobias", 35)

human.add_friend("Robert")
human.add_friend("Sarah")
human.add_friend("John")
human.add_friend("Mike")
human.add_friend("Tom")
human.add_friend("Jen")

human.speak()

print(human)