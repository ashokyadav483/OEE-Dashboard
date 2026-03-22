import streamlit as st

st.title("OEE Dashboard")

# Inputs
availability = st.slider("Availability (%)", 0, 100, 90)
performance = st.slider("Performance (%)", 0, 100, 85)
quality = st.slider("Quality (%)", 0, 100, 95)

# OEE Calculation
oee = (availability * performance * quality) / 10000

st.metric("OEE (%)", round(oee, 2))

# Status
if oee > 85:
    st.success("Excellent Performance")
elif oee > 60:
    st.warning("Average Performance")
else:
    st.error("Needs Improvement")
