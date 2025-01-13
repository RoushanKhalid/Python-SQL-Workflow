# Python-SQL-Workflow

## Overview
**Python-SQL-Workflow** is a project that demonstrates the integration of Python with SQL databases to perform basic CRUD operations. The project is designed to help users understand the fundamental SQL commands and how to implement them using Python. It covers user registration, login, profile viewing, editing, and deletion functionalities.

## Features
- **User Registration:** Allows new users to register by providing their name, email, and password.
- **User Login:** Existing users can log in using their credentials.
- **View Profile:** Logged-in users can view their profile details.
- **Edit Profile:** Users can update their name, email, and password.
- **Delete Profile:** Users can delete their profile from the database.

## Technologies Used
- **Python**: The core programming language used to implement the project logic.
- **MySQL**: The database system used to store user information.
- **MySQL Connector**: A Python library that facilitates the connection and interaction with the MySQL database.

## File Structure
- `Main.py`: Contains the main class `Daraz` that handles user interactions and calls the respective database functions.
- `Database.py`: Contains the `DBhelper` class that provides methods for database operations like registering, searching, updating, and deleting user information.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Python-SQL-Workflow.git
   cd Python-SQL-Workflow
