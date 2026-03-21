import streamlit as st

st.title('Verlauf der Budgetwerte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Budgetdaten vorhanden. Erstellen Sie ein neues Budget auf der Startseite.')
    st.stop()

# Total costs over time
# Total costs over time
chart_df = data_df.set_index('timestamp')[['total_costs', 'remaining', 'after_saving']]
st.line_chart(data=chart_df)

st.caption('Kosten, verbleibend und nach Sparen über Zeit (CHF)')


