import sys
from Database import DBhelper

class Daraz:
    def __init__(self):
        # Connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        Welcome to Daraz!
        Please choose an option:
        1. Register
        2. Login 
        
        Enter your choice: 
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            print("Invalid input. Please try again.")
            sys.exit(1000)

    def register(self):
        name=input("Enter Name: ")
        email=input("Enter Email: ")
        password=input("Enter Password: ")

        response=self.db.register(name,email,password)

        if response:
            print("Registration Successful")
        else:
            print("Registration Failed")

        self.menu()

    def login(self):
        email=input("Enter Email: ")
        password=input("Enter Password: ")

        data=self.db.search(email,password)

        if len(data)==0:
            print("Incorrect Credentials")
            self.login()
        else:
            print("Login Successful")
            print("Hello",data[0][1],"!!!")
            self.login_menu()

    def login_menu(self):
        input("""
        1. See Profile
        2. Edit Profile
        3. Delete Profile
        4. Logout
        """)

obj=Daraz()