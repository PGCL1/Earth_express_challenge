import streamlit as st
from dashboard.KPIs import getMadridEmissions, getVariation
from dashboard.layout import create_column_line

# Madrid emissions section
st.header('Madrid Emissions')
col1, col2, col3 = st.columns(3)
col1.metric("2025 Emissions",
            value=f"{getMadridEmissions()} kg",
            delta=getVariation())
col2.metric("francisca kpi2",
            value="4 $",
            delta="100%")
col3.metric("francisca kpi3",
            value="5 $",
            delta="-50%")

st.divider()

# Department emissions section
st.header("Department Emissions")  # would be cool to show first, departments with most emissions
create_column_line()  # maybe i can pass instead df here and it iterate through each df['department']
create_column_line()  # maybe i can pass instead df here and it iterate through each df['department']
