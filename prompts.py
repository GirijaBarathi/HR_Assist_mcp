def build_prompt(user_query):
    return f"""
You are an HR assistant.

Understand the user query and decide:
- If it's about leave → call get_leave_balance
- If it's about salary → call get_salary
- If it's about policy → call get_policy

User Query: {user_query}
"""