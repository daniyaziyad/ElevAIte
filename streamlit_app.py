import streamlit as st

st.set_page_config(page_title="ElevAIte", layout="wide")

st.title("🚀 ElevAIte Smart Elevator Management System")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Active Elevators", "3")
col2.metric("Energy Saved", "28%")
col3.metric("Current Demand", "High")
col4.metric("Priority Requests", "2")

st.header("AI Recommendations")

st.success("Activate Elevator 4 at 7:50 AM")
st.success("Move Elevator 2 to Ground Floor before class change")
st.success("Keep Elevator 3 in standby mode until 2 PM")

st.header("About ElevAIte")

st.write("""
ElevAIte uses AI to predict elevator demand based on class schedules,
occupancy patterns, and historical data. The system automatically
switches elevators between active and standby modes to reduce energy
consumption while maintaining accessibility and low waiting times.
""")
st.write("""
ElevAIte uses AI to predict elevator demand based on class schedules,
occupancy patterns, and historical data. The system automatically
switches elevators between active and standby modes to reduce energy
consumption while maintaining accessibility and low waiting times.
""")

# PASTE HERE ↓↓↓

import pandas as pd

st.header("Elevator Status")

elevator_data = pd.DataFrame({
    "Elevator": ["A", "B", "C", "D"],
    "Status": ["Active", "Active", "Standby", "Standby"],
    "Current Floor": ["Ground", "Floor 2", "Floor 4", "Floor 3"]
})

st.table(elevator_data)

st.header("Predicted Demand")

demand = pd.DataFrame({
    "Time": ["8 AM", "10 AM", "12 PM", "2 PM", "5 PM"],
    "Demand": [90, 60, 80, 30, 95]
})

st.line_chart(demand.set_index("Time"))

st.header("Energy Consumption Comparison")

energy = pd.DataFrame({
    "System": ["Traditional", "ElevAIte"],
    "Usage": [100, 72]
})

st.bar_chart(energy.set_index("System"))

st.header("Accessibility Monitoring")

st.info("""
Priority services are automatically provided for:
- Wheelchair users
- Elderly visitors
- Injured students
- Temporary mobility assistance requests
""")
