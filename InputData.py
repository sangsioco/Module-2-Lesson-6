# Task 1 Input length validator

def check_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Name lengths are valid.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

check_name_length(first_name, last_name)
    

# Task 2 Password complexity checker

def check_password_complexity(password):
    if len(password) < 8:
        print("Error: Password should be at least 8 characters long.")
        return False

    if not any(char.isupper() for char in password):
        print("Error: Password should contain at least one uppercase letter.")
        return False

    if not any(char.islower() for char in password):
        print("Error: Password should contain at least one lowercase letter.")
        return False

    if not any(char.isdigit() for char in password):
        print("Error: Password should contain at least one digit.")
        return False

    print("Password complexity requirements met.")
    return True

def get_valid_password():
    while True:
        password = input("Enter your password: ")
        if check_password_complexity(password):
            return password
        print("Please try again.")

# Example usage:
password = get_valid_password()


# Task 3 Email formatter

import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        print("Email address is in standard format.")
        return True
    else:
        print("Error: Email address is not in standard format.")
        return False

# Example usage:
email = input("Enter your email address: ")
validate_email(email)


