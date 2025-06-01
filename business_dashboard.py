import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Setup and Logo
st.set_page_config(page_title="Business Calculator", layout="centered")
st.title("Future Business Center")

# 2. Data Entry for Revenue
st.subheader(" Enter Revenue Items")
revenue_data = []
num_revenue = st.number_input("How many revenue items?", min_value=1, max_value=10, step=1)

for i in range(num_revenue):
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input(f"Revenue Item {i+1}", key=f"rev_name_{i}")
    with col2:
        amount = st.number_input(f"AED", key=f"rev_amt_{i}", min_value=0.0, step=100.0)
    revenue_data.append({"Item": name, "Amount": amount})

revenue_df = pd.DataFrame(revenue_data)

# 3. Data Entry for Expenses
st.subheader(" Enter Expense Items")
expense_data = []
num_expense = st.number_input("How many expense items?", min_value=1, max_value=10, step=1)

for i in range(num_expense):
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input(f"Expense Item {i+1}", key=f"exp_name_{i}")
    with col2:
        amount = st.number_input(f"AED ", key=f"exp_amt_{i}", min_value=0.0, step=100.0)
    expense_data.append({"Item": name, "Amount": amount})

expense_df = pd.DataFrame(expense_data)

# 4. Calculate Totals
total_revenue = revenue_df["Amount"].sum()
total_expenses = expense_df["Amount"].sum()
profit = total_revenue - total_expenses
profit_percent = (profit / total_revenue) * 100 if total_revenue > 0 else 0

# 5. Results
st.subheader(" Summary")
st.write(f"**Total Revenue:** AED {total_revenue:,.2f}")
st.write(f"**Total Expenses:** AED {total_expenses:,.2f}")

if profit >= 0:
    st.success(f"Profit: AED {profit:,.2f} ({profit_percent:.2f}%)")
else:
    st.error(f" Loss: AED {abs(profit):,.2f} ({abs(profit_percent):.2f}%)")


import plotly.graph_objects as go

# 6. Interactive Visualization with Profit Included
st.subheader(" Revenue vs Expenses vs Profit")

fig = go.Figure(data=[
    go.Bar(
        name="Revenue",
        x=["Revenue"],
        y=[total_revenue],
        marker_color="rgb(93, 173, 226)",  # Light blue
        text=[f"AED {total_revenue:,.2f}"],
        textposition="auto",
        hovertemplate='Revenue: %{y:.2f} AED'
    ),
    go.Bar(
        name="Expenses",
        x=["Expenses"],
        y=[total_expenses],
        marker_color="rgb(52, 152, 219)",  # Medium blue
        text=[f"AED {total_expenses:,.2f}"],
        textposition="auto",
        hovertemplate='Expenses: %{y:.2f} AED'
    ),
    go.Bar(
        name="Profit",
        x=["Profit"],
        y=[profit],
        marker_color="rgb(40, 116, 166)",  # Dark blue
        text=[f"AED {profit:,.2f}"],
        textposition="auto",
        hovertemplate='Profit: %{y:.2f} AED'
    )
])

fig.update_layout(
    barmode='group',
    yaxis_title="Amount (AED)",
    title="Business Financial Overview",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

