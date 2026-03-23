import os
from dotenv import load_dotenv

from tools import get_leave_balance, get_salary, get_policy

# Load env
load_dotenv(dotenv_path=".env", override=True)


def parse_query(user_input):
    """Local query parser - no API calls needed"""
    user_lower = user_input.lower()
    emp_id = extract_number(user_input)
    
    # Check what the user is asking about
    if any(word in user_lower for word in ["leave", "vacation", "day off", "balance"]):
        return ("get_leave_balance", emp_id)
    
    elif any(word in user_lower for word in ["salary", "pay", "wage", "income"]):
        return ("get_salary", emp_id)
    
    elif any(word in user_lower for word in ["policy", "maternity", "sick", "paternity"]):
        if "maternity" in user_lower:
            return ("get_policy", "maternity")
        elif "sick" in user_lower:
            return ("get_policy", "sick")
        elif "paternity" in user_lower:
            return ("get_policy", "paternity")
        return ("get_policy", None)
    
    return (None, None)


def process_query(user_input):
    action, value = parse_query(user_input)
    print(f"DEBUG: Action={action}, Value={value}")

    if action == "get_leave_balance" and value:
        return get_leave_balance(value)

    elif action == "get_salary" and value:
        return get_salary(value)

    elif action == "get_policy" and value:
        return get_policy(value)

    return "Sorry, I couldn't process that. Try asking about leaves, salary, or policies with an employee ID."


def extract_number(text):
    for word in text.split():
        if word.isdigit():
            return int(word)
    return None


# Run loop
if __name__ == "__main__":
    print("AI HR Assistant (OpenAI Enabled)")

    while True:
        user_input = input("\nAsk: ")
        if user_input.lower() == "exit":
            break

        response = process_query(user_input)
        print("AI:", response)