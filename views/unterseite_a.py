import streamlit as st

st.title('Verlauf der Budgetwerte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Budgetdaten vorhanden. Erstellen Sie ein neues Budget auf der Startseite.')
    st.stop()

# Total costs over time
st.line_chart(data=data_df.set_index('timestamp')['total_costs'])
st.caption('Gesamtkosten über Zeit (CHF)')


