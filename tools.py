from data import employees

def get_leave_balance(emp_id):
    emp = employees.get(emp_id)
    if emp:
        return f"{emp['name']} has {emp['leave_balance']} leave days remaining."
    return "Employee not found."

def get_salary(emp_id):
    emp = employees.get(emp_id)
    if emp:
        return f"{emp['name']}'s salary is {emp['salary']} INR."
    return "Employee not found."

def get_policy(policy_name):
    policies = {
        "maternity": "Maternity leave is 26 weeks as per company policy.",
        "sick": "Employees are entitled to 10 sick leaves per year."
    }
    return policies.get(policy_name.lower(), "Policy not found.")