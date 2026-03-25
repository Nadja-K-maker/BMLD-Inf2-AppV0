from datetime import datetime 
import pytz


def calculate_budget(income, rent, food, other, savings_goal):
    total_costs = rent + food + other
    remaining = income - total_costs
    after_saving = remaining - savings_goal
    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
        "total_costs": total_costs,
        "remaining": remaining,
        "after_saving": after_saving
    }