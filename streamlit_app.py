import streamlit as st

pages = {
    "Your account": [
        st.Page("dashboard/department_emissions.py", title="Stats"),
        st.Page("travel_calculation/app.py", title="Travel Cockpit"),
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
