import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Pocket Smart",
    page_icon="💰",
    layout="wide"
)

# ---------- Recommendation engine ----------
def budget_recommendation(income, expenses, savings_goal, risk_level):
    disposable = income - expenses
    if income <= 0:
        return {
            "status": "Enter a valid monthly income.",
            "savings": 0,
            "spending": 0,
            "emergency": 0,
            "tip": "Monthly income must be greater than zero."
        }

    # Simple 50/30/20-inspired model, adjusted for the user's actual expenses.
    target_savings = max(income * 0.20, savings_goal)
    affordable_savings = max(0, disposable)

    recommended_savings = min(target_savings, affordable_savings)
    recommended_spending = max(0, disposable - recommended_savings)
    emergency_fund = income * 3

    if disposable < 0:
        status = "⚠️ Your expenses are higher than your income."
        tip = "Start by reducing non-essential spending and reviewing recurring subscriptions."
    elif recommended_savings < target_savings:
        status = "🟡 Your savings goal is higher than your current surplus."
        tip = "Consider lowering the goal temporarily or reducing flexible expenses."
    else:
        status = "🟢 Your budget has room for your savings goal."
        tip = "Automate savings immediately after receiving your income."

    if risk_level == "Conservative":
        investment_note = "Prioritize an emergency fund and low-risk savings before investing."
    elif risk_level == "Balanced":
        investment_note = "Build an emergency fund first, then consider diversified investments."
    else:
        investment_note = "After building an emergency fund, you can consider higher-volatility investments based on your risk tolerance."

    return {
        "status": status,
        "savings": recommended_savings,
        "spending": recommended_spending,
        "emergency": emergency_fund,
        "tip": tip,
        "investment_note": investment_note
    }

# ---------- UI ----------
st.title("💰 Pocket Smart")
st.subheader("Smart Budget Recommendation Assistant")
st.write(
    "Enter your monthly financial details and Pocket Smart will generate "
    "a simple, personalized budget recommendation."
)

st.info("Educational tool only — recommendations are general and are not financial advice.")

with st.sidebar:
    st.header("Your Monthly Details")
    income = st.number_input("Monthly income (₹)", min_value=0.0, value=30000.0, step=1000.0)
    expenses = st.number_input("Monthly expenses (₹)", min_value=0.0, value=18000.0, step=500.0)
    savings_goal = st.number_input("Monthly savings goal (₹)", min_value=0.0, value=5000.0, step=500.0)
    risk_level = st.selectbox("Risk preference", ["Conservative", "Balanced", "Growth"])

result = budget_recommendation(income, expenses, savings_goal, risk_level)

col1, col2, col3 = st.columns(3)
col1.metric("Income", f"₹{income:,.0f}")
col2.metric("Current Expenses", f"₹{expenses:,.0f}")
col3.metric("Monthly Surplus", f"₹{income-expenses:,.0f}")

st.divider()

st.subheader("📊 Recommended Monthly Budget")

r1, r2, r3 = st.columns(3)
r1.metric("Recommended Savings", f"₹{result['savings']:,.0f}")
r2.metric("Flexible Spending", f"₹{result['spending']:,.0f}")
r3.metric("Emergency Fund Target", f"₹{result['emergency']:,.0f}")

st.success(result["status"])

st.subheader("💡 Smart Recommendations")
st.write(f"**Savings:** Try to save approximately ₹{result['savings']:,.0f} per month.")
st.write(f"**Spending:** Keep flexible/non-essential spending around ₹{result['spending']:,.0f} or below.")
st.write(f"**Action:** {result['tip']}")
st.write(f"**Risk preference:** {result['investment_note']}")

st.divider()

st.subheader("🧮 Budget Breakdown")
breakdown = pd.DataFrame({
    "Category": ["Current Expenses", "Recommended Savings", "Flexible Spending"],
    "Amount (₹)": [expenses, result["savings"], result["spending"]]
})
st.bar_chart(breakdown.set_index("Category"))

st.subheader("📌 Example Budget Rules")
rules = pd.DataFrame({
    "Rule": [
        "Needs / essential expenses",
        "Savings",
        "Flexible spending",
        "Emergency fund"
    ],
    "Guideline": [
        "Keep essential costs controlled and review recurring bills.",
        "Aim for around 20% of income when affordable.",
        "Use the remaining surplus for discretionary spending.",
        "Build roughly 3 months of income as a long-term target."
    ]
})
st.dataframe(rules, use_container_width=True, hide_index=True)

st.caption("Pocket Smart Project • Built with Python + Streamlit")
