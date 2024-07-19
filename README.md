# Recipe App Command Line Interface

## Overview
This Recipe App is a command-line application designed to create, read, modify, and search for recipes. It serves as a foundation for understanding Python programming, data structures, object-oriented programming, and database interaction, which are crucial for web development with frameworks like Django.

## Objective
The primary objective is to demonstrate proficiency in Python by building a functional CLI application. This project will showcase the ability to handle Python's fundamentals, interact with databases, and follow standard programming practices.

## Features
- **Recipe Management**: Users can create, update, and delete recipes in a locally hosted MySQL database.
- **Search Functionality**: Ability to search for recipes based on ingredients.
- **Difficulty Rating**: Automatic calculation and display of each recipe's difficulty level.
- **Detailed Recipe Display**: Option to view detailed information about recipes, including ingredients, cooking time, and difficulty.

## Technical Requirements
- **Error Handling**: The app will gracefully handle exceptions and errors, providing user-friendly messages.
- **Database Connection**: Utilizes a MySQL database for storing recipe data.
- **User Interface**: Offers an easy-to-use command-line interface with clear instructions and input validation.
- **Compatibility**: Compatible with Python 3.6 and above.
- **Code Quality**: Well-formatted code adhering to standardized guidelines, accompanied by meaningful comments.

## Installation and Setup
1. **Python Installation**: Ensure Python 3.6+ is installed on your system.
2. **Virtual Environment**:
   - Create a virtual environment: `python3 -m venv venv`
   - Activate the virtual environment:
	 - Windows: `.\venv\Scripts\activate`
	 - macOS/Linux: `source venv/bin/activate`
3. **Dependencies**: Install required packages: `pip install -r requirements.txt`
4. **Database Setup**: Set up a local MySQL database and update the connection details in the application configuration.

## Usage
- Run the application: `python app.py`
- Follow the on-screen instructions to manage and search for recipes.

## Project Structure
- `app.py`: Entry point of the application.
- `models.py`: Defines the Recipe class and database schema.
- `database.py`: Handles database connections and operations.
- `requirements.txt`: Lists all the necessary Python packages.

## Contributing
Contributions to the Recipe App are welcome. Please follow the standard fork-and-pull request workflow.

## License
This project is licensed under the MIT License - see the LICENSE file for details.