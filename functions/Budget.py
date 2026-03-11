from datetime import datetime 
import pytz
def calculate_costs(income, rent, food, other, savings_goal):
    total_costs = rent + food + other
    remaining = income - total_costs
    after_saving = remaining - savings_goal
    return total_costs, remaining, after_saving

# Code return, soll als Dictionary zurückgegeben
def calculate_budget(income, rent, food, other, savings_goal):
    total_costs = rent + food + other
    remaining = income - total_costs
    after_saving = remaining - savings_goal
    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')).isoformat(),
        "total_costs": total_costs,
        "remaining": remaining,
        "after_saving": after_saving
    }