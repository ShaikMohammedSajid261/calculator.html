# User authentication system using Python

# Define the user database (a simple text file)
USER_DATABASE = "user_db.txt"

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the username already exists
    with open(USER_DATABASE, "r") as file:
        for line in file:
            if username in line:
                print("Username already exists. Please choose a different one.")
                return

    # Store the new user's credentials
    with open(USER_DATABASE, "a") as file:
        file.write(f"{username}:{password}\n")
    print("Registration successful.")

# Function to log in a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    with open(USER_DATABASE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Login successful.")
                return

    print("Login failed. Please check your credentials.")

# Main program
while True:
    print("\nWelcome to the User Authentication System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
