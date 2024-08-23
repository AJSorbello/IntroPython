
```markdown
# Pre-Work: Before You Start the Course

## Reflection Questions (to complete before your first mentor call)

1. What experiences have you had with coding and/or programming so far? What other experiences (programming-related or not) have you had that may help you as you progress through this course?

Answer:  - I haven't had any coding experience prior to CareerFoundry. I have completed Full Stack Immersion, which covers the MEARN and MEAN stack. Check out my portfolio [here](https://ajsorbello.github.io/AJfolio/). My experience in staying focused and completing tasks comes from working at computer/desk jobs for the last 20+ years in sales, customer service, creative arts, using LOS/POS, CRM, DAWs, marketing tools, and many other software creative tools.

2. What do you know about Python already? What do you want to know?

Answer: - I know that Python is a programming language used for various applications like video games, AI, and machine learning. I understand that many jobs require Python experience, and I want to learn more about it.

3. What challenges do you think may come up while you take this course? What will help you face them? Think of specific spaces, people, and times of day or week that might be favorable for facing challenges and growing. Plan for how to solve challenges that arise.

Answer: - Like any new language, there is a learning curve. Staying focused on the course and overcoming challenges is key. When I encounter a problem, I will analyze it and work through various possible solutions until I find the right method.

*Remember, you can always refer to Exercise 1.4 of the Orientation course if you’re not sure whom to reach out to for help and support.*

# Exercise 1.1: Getting Started with Python

### Learning Goals

- Summarize the uses and benefits of Python for web development
- Prepare your developer environment for programming with Python

### Reflection Questions

1. In your own words, what is the difference between frontend and backend web development? If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?

Answer:  - Frontend is the part of the website that the user sees and interacts with. Backend is what the user does not see, including the infrastructure and data management that power the frontend. Backend operations handle data storage, retrieval, updates, user authentication, business logic, and server configuration. Database management involves designing, creating, and managing databases to store and retrieve data. Server-side logic involves writing server-side code that handles requests from the frontend, processes data, and sends appropriate responses back. API development includes creating and maintaining application programming interfaces for the frontend to interact with backend services. Authentication involves implementing user authentication to ensure secure access to applications. Performance optimization ensures that backend services run efficiently and can handle high traffic loads. Integration with third-party services involves connecting the application with external services, such as payment gateways and third-party APIs.

2. Imagine you’re working as a full-stack developer in the near future. Your team is asking for your advice on whether to use JavaScript or Python for a project, and you think Python would be the better choice. How would you explain the similarities and differences between the two languages to your team? Drawing from what you learned in this exercise, what reasons would you give to convince your team that Python is the better option? *(Hint: refer to the exercise section “The Benefits of Developing with Python”)*

Answer: -  Let's use Python for our project. Although JavaScript is capable of achieving the same functionalities we need, Python's syntax is much easier to write and read, which will be beneficial for our team. For example, to perform a simple calculation like 
𝑎
+
𝑏
a+b, in JavaScript, we might need to create a function and handle additional complexities. In Python, we can simply write c = a + b on a single line. This simplicity not only speeds up our development process but also reduces the likelihood of errors, making our codebase easier to maintain and extend. Moreover, Python has extensive libraries and frameworks that can help us handle various tasks more efficiently, from data analysis to machine learning, providing us with more flexibility and power for future project needs.

3. Now that you’ve had an introduction to Python, write down 3 goals you have for yourself and your learning during this Achievement. You can reflect on the following questions if it helps you. What do you want to learn about Python? What do you want to get out of this Achievement? Where or what do you see yourself working on after you complete this Achievement?

Answer: - 

Learn Python for Web Development

I want to learn how to use Python to create web applications. My specific goal is to build a mortgage calculator. To achieve this, I need to understand Python's basics like variables, data types, loops, conditionals, functions, and object-oriented programming. This will give me a solid foundation for more advanced Python tasks.

Complete Practical Projects Using Python

I aim to complete several hands-on projects using Python. These projects could include things like simple websites, data analysis tools, or automation scripts. Working on real projects will help me understand how to apply what I’ve learned and gain practical experience.

Prepare for a Job in Software Development

My ultimate goal is to be ready for a job in software development where I can use Python. I want to be good enough at Python to confidently apply for jobs that need Python skills. I also plan to create a portfolio of Python projects to show potential employers what I can do.
These goals will help me stay focused and motivated. After completing this course, I see myself working in a job where I can create useful software solutions, possibly in web development or data analysis, using Python.
```
# Exercise 1.2: Data Types in Python

### Learning Goals
- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

### Reflection Questions

1. **Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

   **Answer:** The iPython Shell has several advantages over Python's default shell:
   - Autocompletion
   - Easier access to shell commands
   - Input/output history across sessions

2. **Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

   | Data Type  | Definition                                                         | Scalar or Non-Scalar? |
   |------------|--------------------------------------------------------------------|-----------------------|
   | Integer    | A whole number, positive or negative, without decimals             | Scalar                |
   | String     | A sequence of characters, used to represent text                   | Non-Scalar            |
   | List       | An ordered collection of elements that can be of different types   | Non-Scalar            |
   | Dictionary | A collection of key-value pairs, where each key is unique          | Non-Scalar            |

3. **A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

   **Answer:** Lists and tuples are both data structures in Python that can store multiple values. However, lists are mutable, meaning the elements can be changed after creation, whereas tuples are immutable and cannot be changed once created. Lists use square brackets `[ ]`, while tuples use parentheses `( )`. Performance-wise, tuples are generally faster than lists because they are immutable. Lists are used when you need a collection of items that may need to be modified, and tuples are used when you want to ensure data remains constant.

4. **In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

   **Answer:** For the language-learning app, I would choose dictionaries because this structure allows easy access and modification and is more flexible when needing to add additional attributes in the future like usage frequency and example sentences. Lists or tuples would not be as efficient because they don't provide named keys for easy access and modification.

# Exercise 1.3: Functions and Other Operations in Python

## Learning Goals
- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

## 1: Reflection Questions

In this exercise, you learned how to use `if-elif-else` statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an `if-elif-else` statement for the following situation:

1. The script should ask the user where they want to travel.
2. The user’s input should be checked for 3 different travel destinations that you define.
3. If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
4. If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”

### Write your script here. (Hint: remember what you learned about indents!)


## Asking the user where they want to travel
```python
destination = input("Where do you want to travel? ")
```
## Defining three travel destinations
```python
destination_1 = "Paris"
destination_2 = "New York"
destination_3 = "Tokyo"
```

## Checking user's input and printing appropriate message
```python
if destination == destination_1:
    print("Enjoy your stay in Paris!")
elif destination == destination_2:
    print("Enjoy your stay in New York!")
elif destination == destination_3:
    print("Enjoy your stay in Tokyo!")
else:
    print("Oops, that destination is not currently available.")
```
## 2: Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.

Logical operators in Python are used to combine conditional statements. There are three logical operators:

-  and: Returns True if both statements are true.
Example: a and b returns True only if both a and b are True.
-  or: Returns True if one of the statements is true.
Example: a or b returns True if either a or b is True.
-  not: Reverses the result, returns False if the result is true.
Example: not a returns True if a is False.

## 3: What are functions in Python? When and why are they useful?

Functions in Python are defined using the def keyword. A function is a block of code that only runs when it is called. Functions help to break the code into smaller and modular chunks. They can accept inputs, perform specific tasks, and return outputs.

### When and why are functions useful?

Modularity: They help divide a complex problem into smaller, manageable pieces.
Reusability: Once a function is defined, it can be reused multiple times in a program, reducing code redundancy.
Readability: Functions make the code more organized and easier to read and understand.
Maintainability: Functions make it easier to update and maintain the code since changes in functionality can be made within the function without affecting the entire codebase.
In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

## For the preparation of your next mentor call, consider reflecting on the following points:

## 4: Progress Towards Goals: 

Progress:

So far, I have completed all exercises and reflection questions for Exercise 1.3, focusing on conditional statements, loops, and functions in Python. My initial goals were to strengthen my understanding of Python basics and write cleaner code, which the exercises have helped achieve. I faced challenges with if-elif-else statements and writing functions but overcame them through practice and additional resources. As a result, I've improved my code structure, problem-solving skills, and understanding of logical operators. Next, I plan to continue practicing, explore advanced Python topics, and develop a small project to apply my learning.


### Exercise 1.4: File Handling in Python

#### Learning Goals
- Use files to store and retrieve data in Python.

#### Reflection Questions

**Why is file storage important when you’re using Python? What would happen if you didn’t store local files?**

**Answer:** File storage is important in Python for several reasons:

- **Persistence:** It allows data to persist beyond the execution of the program. Without file storage, all data would be lost once the program terminates.
- **Data Management:** Storing data in files helps in managing large amounts of data efficiently. It also facilitates data sharing between different programs and users.
- **Backup and Recovery:** Files provide a way to backup data, which can be recovered in case of system failures.

Without local file storage, you would have to rely on in-memory data structures which are not suitable for long-term data storage or for sharing data between different programs. Once the program ends, all data would be lost, making it impossible to maintain state or history.

**In this exercise, you learned about the pickling process with the `pickle.dump()` method. What are pickles? In which situations would you choose to use pickles and why?**

**Answer:** Pickles are a way to serialize and deserialize Python object structures. Using the `pickle` module, you can convert Python objects into a byte stream (`pickle.dump()`) and later convert the byte stream back into Python objects (`pickle.load()`).

**Situations to use pickles:**

- **Storing Complex Data Types:** Pickle is useful for storing complex data types like lists, dictionaries, or custom objects.
- **Quick Serialization:** It provides a quick way to serialize and deserialize Python objects, which is useful for saving program state or data caching.
- **Python-Specific Use:** It's particularly useful when the data will only be read and written by Python programs since it’s specific to Python.

**In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?**

**Answer:** To find out the current working directory, you use the `os.getcwd()` function from the `os` module. To change the current working directory, you use the `os.chdir()` function.

```
import os
current_directory = os.getcwd()  # Get current working directory
print("Current Directory:", current_directory)

os.chdir('/path/to/new/directory')  # Change current working directory
print("Directory Changed To:", os.getcwd())
```

Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

Answer: To prevent the entire script from terminating due to an error, you can use a try-except block. This allows you to catch and handle exceptions gracefully.

```
python

try:
    # Code that may raise an exception
    risky_code()
except SpecificException as e:
    # Handle specific exception
    print(f"An error occurred: {e}")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # Code to execute if no exceptions were raised
    print("Code executed successfully")
finally:
    # Code to execute regardless of whether an exception was raised or not
    cleanup()
```
You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.

Answer:

Progress Reflection: Reflecting on the course so far, I've learned a lot about Python basics, file handling, and error management.

Proud Moments: I’m proud of my ability to understand and implement file handling techniques and use the pickle module for data serialization.

Challenges: I am struggling a bit with more advanced topics such as complex data structures and their manipulation.

Need More Practice: I need more practice with error handling and understanding how to effectively debug my programs.

Next Steps: In my next mentor call, I would like to discuss strategies for improving my understanding of advanced topics and best practices for debugging Python code.

### Exercise 1.5: Object-Oriented Programming in Python

#### Learning Goals
- Apply object-oriented programming concepts to your Recipe app

#### Reflection Questions

1. **In your own words, what is object-oriented programming? What are the benefits of OOP?**

**Answer:** Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code. Data is represented as attributes (also known as properties or fields), and code is represented as methods (functions that operate on the data). OOP aims to implement real-world entities like inheritance, hiding, polymorphism, and more in programming.

**Benefits of OOP:**

- **Modularity:** Code is organized into classes and objects, making it more modular. This modularity allows for easier maintenance and modification.
- **Reusability:** Once a class is created, it can be reused to create multiple objects, reducing redundancy.
- **Scalability:** OOP makes it easier to manage and scale larger projects by organizing code into manageable sections.
- **Flexibility through Polymorphism:** Polymorphism allows methods to be used interchangeably based on the context, which simplifies code and increases flexibility.
- **Encapsulation:** Encapsulation protects data by restricting access to it, which can prevent accidental modification and promote data integrity.

2. **What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.**

**Answer:**

- **Class:** A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
- **Object:** An object is an instance of a class. It is created using the class and can access the class's attributes and methods.

**Real-world example:**

Consider a class `Car`:

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

An object of the Car class can be created as follows:
```
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Outputs: Brand: Toyota, Model: Corolla, Year: 2020
```

Here, Car is a class, and my_car is an object of the Car class. The my_car object has attributes (brand, model, and year) and can use methods (display_info) defined in the class.

3. In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine.

Method	Description

## Inheritance:
	Inheritance is an OOP concept where a new class (called the child or subclass) is created based on an existing class (called the parent or superclass). The child class inherits attributes and methods from the parent class, allowing for code reuse and the creation of a hierarchical relationship between classes. This helps in reducing redundancy and promotes the reuse of existing code. For example, a Dog class can inherit from an Animal class, gaining its attributes and behaviors while adding specific dog-related features.

## Polymorphism:
	Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is the ability to redefine methods for derived classes. This means that a single method can operate differently on different objects. For example, a method make_sound can be defined in a parent class Animal and overridden in subclasses Dog and Cat. When called, make_sound will produce a different sound based on whether it is invoked on a Dog object or a Cat object. This allows for flexibility and the use of a single interface to interact with different types of objects.
    
## Operator Overloading:
	Operator overloading is the ability to define custom behavior for operators (such as +, -, *, etc.) for user-defined classes. This allows objects of custom classes to interact using standard operators. For example, in a Vector class, you can overload the + operator to allow the addition of two Vector objects. This is done by defining the __add__ method within the class. Operator overloading makes code more intuitive and easier to read, as it allows for natural expressions and operations on objects.

By applying these OOP concepts, you can create a more organized, reusable, and maintainable code structure in your Recipe app or any other software project.


## Exercise 1.6: Learning Goals
- Create a MySQL database for your Recipe app.

## Reflection Questions

### 1. What are databases and what are the advantages of using them?
**Databases:** Databases are structured collections of data that are stored and managed electronically. They are used to store, retrieve, and manage data efficiently.

**Advantages:**
- **Data Integrity:** Databases help ensure that data is accurate and consistent over time.
- **Data Security:** They provide mechanisms for securing data, including access controls and encryption.
- **Scalability:** Databases can handle large volumes of data and complex queries, allowing applications to scale.

### 2. List 3 data types that can be used in MySQL and describe them briefly:
- **VARCHAR:** A variable-length string data type. It stores alphanumeric data and is often used for storing text with a variable length up to a specified limit.
- **INT:** An integer data type. It stores whole numbers without decimals, often used for counting or identifiers.
- **DATE:** A date data type. It stores dates in the format YYYY-MM-DD and is used for date-related fields.

### 3. In what situations would SQLite be a better choice than MySQL?
SQLite is better suited for:
- **Single-user applications:** Where the database needs to be lightweight and doesn’t require the overhead of a full database server.
- **Prototyping:** When quickly setting up a database for development or testing purposes without the need for complex setup.
- **Embedded systems:** Where storage space is limited, and the application requires a self-contained database.

### 4. Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?
- **JavaScript:** Primarily used for web development, both on the client-side (in the browser) and server-side (with Node.js). It’s known for its event-driven, non-blocking I/O model, which is great for handling asynchronous operations.
- **Python:** A versatile, high-level programming language known for its readability and simplicity. It’s widely used for web development, data analysis, AI, machine learning, and more. Python emphasizes code readability and allows developers to express concepts in fewer lines of code compared to JavaScript.

### 5. Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?
- **Performance:** Python is generally slower than compiled languages like C++ or Java because it’s an interpreted language.
- **Mobile Development:** Python is not as commonly used for mobile application development compared to languages like Swift or Kotlin.
- **Global Interpreter Lock (GIL):** In CPython, the most common implementation of Python, the GIL can be a bottleneck in CPU-bound and multithreaded programs, limiting the performance of concurrent threads.

These questions are designed to help you reflect on the material and ensure you have a strong grasp of the concepts related to databases and the Python programming language. Let me know if you need further clarification or if there's anything specific you want to dive deeper into!

## Reflection Questions

### What is an Object Relational Mapper (ORM) and what are the advantages of using one?

**Response:** An Object Relational Mapper (ORM) is a tool that allows developers to interact with a database using an object-oriented paradigm instead of writing SQL queries directly. The primary advantages include:
- **Abstraction:** Simplifies database interactions by allowing developers to work with Python objects rather than raw SQL queries.
- **Portability:** Makes it easier to switch between different databases by abstracting the database layer.
- **Productivity:** Reduces the amount of boilerplate code, enabling faster development.
- **Security:** Helps prevent SQL injection attacks by automatically handling query parameters.

### By this point, you’ve finished creating your Recipe app. How did it go? What’s something in the app that you did well with? If you were to start over, what’s something about your app that you would change or improve?

**Response:** The development of the Recipe app went smoothly overall. One thing I did well was setting up the database models and implementing the authentication flow. If I were to start over, I would focus on improving the user interface to make it more intuitive and perhaps add more robust error handling throughout the app to improve user experience.

### Imagine you’re at a job interview. You’re asked what experience you have creating an app using Python. Taking your work for this Achievement as an example, draft how you would respond to this question.

**Response:** "During my recent project, I developed a command-line Recipe application using Python and SQLAlchemy as the ORM. The application allows users to create, view, edit, and delete recipes while storing data in a MySQL database. I implemented user authentication, ensuring secure access to the application's features. Additionally, I integrated various functionalities such as searching by ingredients, dynamically calculating recipe difficulty, and managing user profiles. This project gave me hands-on experience with Python, database interactions, and building scalable applications."

### You’ve finished Achievement 1! Before moving on to Achievement 2, take a moment to reflect on your learning in the course so far:

#### What went well during this Achievement?
The structured approach to building the app, starting from setting up the database to implementing user features, went very well. The clear guidance on each step made the process manageable.

#### What’s something you’re proud of?
I’m proud of successfully integrating the ORM with the command-line interface, which made interacting with the database seamless.

#### What was the most challenging aspect of this Achievement?
The most challenging aspect was managing the different states of the application, especially ensuring that the database interactions were efficient and error-free.

#### Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Python skills?
Yes, this Achievement exceeded my expectations. It reinforced my understanding of Python and databases, and I now feel confident in applying these skills to real-world projects.

#### What’s something you want to keep in mind to help you do your best in Achievement 2?
I want to keep in mind the importance of testing and validating each part of the application as I build it. This will help in catching issues early and ensuring a smooth development process.

