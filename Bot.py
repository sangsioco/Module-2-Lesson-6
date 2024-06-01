# Task 1 Command parser

def process_command(text):
    commands = {
        "help": "Sure, I can help you. What do you need assistance with?",
        "issue": "Please describe the issue you're facing in detail.",
        "contact support": "You can contact our support team at support@example.com."
    }
    
    for command, response in commands.items():
        if command in text:
            print(response)
            return True
    
    return False

user_input = input("Enter your text: ")
if not process_command(user_input):
    print("No predefined command found.")

# Task 2 Issue categorizer  
    if "issue" in text:
        return categorize_issue(text)
    
    return False

def categorize_issue(text):
    categories = {
        "login": ["login", "authentication", "signin"],
        "performance": ["performance", "slow", "lag"],
        "error": ["error", "issue", "problem"],
        # Add more categories and corresponding keywords as needed
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                print(f"The issue is categorized as: {category}")
                return True
    
    return False

user_input = input("Enter your text: ")
if not process_command(user_input):
    print("No predefined command found.")



