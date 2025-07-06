import streamlit as st
import pandas as pd
import numpy as np
from dashboard.utils import get_kpi_variation, KPI

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


# function to create a 3-columns on the same line
# TODO: find a way to make columns clickable
def create_column_line():
    for col in st.columns(3, border=True):
        with col:
            st.metric(label="Test",
                      value=6666,
                      delta="+1%")
            st.line_chart(chart_data)
            st.markdown("[Further information](https:://www.google.com)")


# def create_KPI(KPI: object, col):
#    with col:
#        st.metric(label=KPI.name,
#                  value=KPI.value,
#                  delta=KPI.variation)

# def arrange_column(col, department: object):
#    st.metric(label=department.name,
#              value=department.emissions,
#              delta=get_department_emissions(),
#              border=True)
