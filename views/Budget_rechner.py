import pandas as pd  # --- NEW CODE: add pandas to the imports ---
import streamlit as st
from functions.Budget import calculate_costs
#import panda as pd

st.title("Budget-Rechner")

income = st.number_input("Einkommen (CHF)", min_value=0.0, step=50.0)
rent = st.number_input("Miete (CHF)", min_value=0.0, step=50.0)
food = st.number_input("Essen (CHF)", min_value=0.0, step=10.0)
other = st.number_input("Sonstiges (CHF)", min_value=0.0, step=10.0)
savings_goal = st.number_input("Sparziel (CHF)", min_value=0.0, step=50.0)

if st.button("Budget berechnen"):
    total_costs, remaining, after_saving = calculate_costs(
        income, rent, food, other, savings_goal)

    st.subheader("Ergebnis")
    st.write("Total Kosten:", f"{total_costs:.2f} CHF")
    st.write("Übrig:", f"{remaining:.2f} CHF")
    st.write("Übrig nach Sparziel:", f"{after_saving:.2f} CHF")

    if remaining < 0:
        st.error("Du gibst mehr aus als du einnimmst.")
    elif after_saving < 0:
        st.warning("Mit diesem Sparziel wird es knapp.")
    else:
        st.success("Budget passt gut! Du kannst dein Sparziel erreichen.")

