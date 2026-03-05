def calculate_costs(income, rent, food, other, savings_goal):
    total_costs = rent + food + other
    remaining = income - total_costs
    after_saving = remaining - savings_goal
    return total_costs, remaining, after_saving