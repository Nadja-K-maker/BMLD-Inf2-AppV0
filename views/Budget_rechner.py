from unittest import result

import pandas as pd  # --- NEW CODE: add pandas to the imports ---
import streamlit as st
from functions.Budget import calculate_budget, calculate_costs

st.title("Budget-Rechner")

income = st.number_input("Einkommen (CHF)", min_value=0.0, step=50.0)
rent = st.number_input("Miete (CHF)", min_value=0.0, step=50.0)
food = st.number_input("Essen (CHF)", min_value=0.0, step=10.0)
other = st.number_input("Sonstiges (CHF)", min_value=0.0, step=10.0)
savings_goal = st.number_input("Sparziel (CHF)", min_value=0.0, step=50.0)

if st.button("Budget berechnen"):
    total_costs, remaining, after_saving = calculate_costs(
        income, rent, food, other, savings_goal)

    result = calculate_budget(income, rent, food, other, savings_goal)
    st.subheader("Ergebnis")
    st.write("Total Kosten:", f"{total_costs:.2f} CHF")
    st.write("Übrig:", f"{remaining:.2f} CHF")
    st.write("Übrig nach Sparziel:", f"{after_saving:.2f} CHF")
    st.write("Berechnet am:", result["timestamp"].strftime("%d.%m.%Y %H:%M:%S"))

    if remaining < 0:
        st.error("Du gibst mehr aus als du einnimmst.")
    elif after_saving < 0:
        st.warning("Mit diesem Sparziel wird es knapp.")
    else:
        st.success("Budget passt gut! Du kannst dein Sparziel erreichen.")



from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
 
st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])])
 
 #  CODE UPDATE: save data to data manager ---
data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---

# display the data frame in a table
st.dataframe(st.session_state['data_df'])
