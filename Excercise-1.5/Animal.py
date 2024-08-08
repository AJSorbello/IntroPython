class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    # Getter methods for age and name       
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # Setter methods for age and name
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # String representation of the Animal class
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


class Cat(Animal):
    # Initialize the Cat class
    def __init__(self, age):
        super().__init__(age)

    # Cat's speak method
    def speak(self):
        print("Meow")

    # String representation of the Cat class
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


class Dog(Animal):
    # Initialize the Dog class
    def __init__(self, age):
        super().__init__(age)

    # Dog's speak method
    def speak(self):
        print("Woof!")

    # String representation of the Dog class
    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

class Human(Animal):
    # Initialize the Human class
    def __init__(self, name, age):
        super().__init__(age)

        # Setting a name, since humans must have names
        self.set_name(name)

        # Our new attribute for humans, 'friends'!
        self.friends = []

    # Method to add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    # Method to display friends
    def show_friends(self):
        for friend in self.friends:
            print(friend)

    # Humans can speak sentences!
    def speak(self):
        print("Hello, my name's " + self.name + "!")

    # String representation of the Human class
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
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

# Creating an instance of Human
human = Human("Tobias", 35)

# Adding friends to the human
human.add_friend("Robert")
human.add_friend("Sarah")
human.add_friend("John")
human.add_friend("Mike")
human.add_friend("Tom")
human.add_friend("Jen")

# Printing the human object
print(human)
# Human speaks
human.speak()