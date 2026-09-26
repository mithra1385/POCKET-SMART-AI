# Pocket Smart – Project Document

## 1. Project Title

**Pocket Smart – Smart Budget Recommendation Assistant**

## 2. Abstract

Pocket Smart is a web-based smart budgeting assistant designed to help users understand their monthly cash flow and create a simple savings and spending plan.

The user enters monthly income, expenses, savings goal, and risk preference. The system calculates the monthly surplus and provides budget recommendations using a transparent rule-based recommendation engine.

The project is designed as a beginner-friendly prototype that can be deployed through GitHub and Streamlit Community Cloud.

## 3. Problem Statement

Many users find it difficult to determine how much they should save and how much they can safely spend each month.

Pocket Smart addresses this problem by converting basic financial inputs into a simple and understandable monthly budget recommendation.

## 4. Objectives

1. Collect basic monthly financial information.
2. Calculate monthly surplus.
3. Recommend a practical savings amount.
4. Estimate flexible spending capacity.
5. Provide an emergency-fund target.
6. Provide simple guidance based on risk preference.
7. Present the results through an easy-to-use dashboard.

## 5. Target Users

- Students
- Young professionals
- First-time budget planners
- Users who want a simple personal finance dashboard

## 6. Functional Requirements

### Input

- Monthly income
- Monthly expenses
- Monthly savings goal
- Risk preference

### Processing

- Calculate monthly surplus.
- Calculate recommended savings.
- Calculate flexible spending.
- Calculate emergency-fund target.
- Generate recommendation messages.

### Output

- Income summary
- Expense summary
- Surplus
- Recommended savings
- Flexible spending
- Emergency-fund target
- Smart recommendations
- Budget chart

## 7. Non-Functional Requirements

- Simple user interface
- Fast response
- Easy deployment
- Transparent recommendation logic
- Beginner-friendly code
- No external financial account required

## 8. System Architecture

```text
User
  |
  v
Streamlit Web Interface
  |
  v
Input Validation
  |
  v
Budget Recommendation Engine
  |
  +--> Savings Recommendation
  |
  +--> Flexible Spending
  |
  +--> Emergency Fund
  |
  v
Dashboard / Charts
```

## 9. Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend / Logic | Python |
| Data Processing | Pandas |
| Source Control | GitHub |
| Deployment | Streamlit Community Cloud |

## 10. Recommendation Logic

Let:

`Surplus = Monthly Income - Monthly Expenses`

A target savings value is calculated from approximately 20% of income and the user's savings goal.

The recommended savings amount is limited by the actual monthly surplus.

`Recommended Savings = min(Target Savings, Monthly Surplus)`

The remaining surplus is treated as flexible spending:

`Flexible Spending = Monthly Surplus - Recommended Savings`

The long-term emergency-fund target is:

`Emergency Fund Target = Monthly Income × 3`

If expenses exceed income, the application warns the user and recommends reducing non-essential spending.

## 11. User Flow

```text
Open Pocket Smart
       |
Enter income
       |
Enter expenses
       |
Enter savings goal
       |
Select risk preference
       |
Click / update inputs
       |
View recommendation
       |
Review budget chart
```

## 12. Testing

### Test Case 1

Input:
- Income: ₹30,000
- Expenses: ₹18,000
- Savings Goal: ₹5,000

Expected:
- Surplus: ₹12,000
- Recommended savings: ₹6,000
- Flexible spending: ₹6,000

### Test Case 2

Input:
- Income: ₹20,000
- Expenses: ₹22,000

Expected:
- Negative surplus warning
- Recommendation to reduce non-essential spending

## 13. Limitations

- It does not connect to bank accounts.
- It does not automatically classify transactions.
- Recommendations are rule-based rather than machine-learning based.
- It does not provide professional financial advice.
- User data is not stored in the first version.

## 14. Future Scope

The project can be extended with:

- AI-powered recommendations
- Expense receipt scanning
- Automatic transaction categorization
- User authentication
- Database storage
- Monthly reports
- Budget notifications
- Goal tracking
- Financial trend analysis
- Mobile-friendly PWA
- Tamil/English language support

## 15. Conclusion

Pocket Smart provides a simple foundation for a smart personal budgeting application. The architecture is intentionally lightweight so that it can be easily uploaded to GitHub, tested, demonstrated, and deployed online.
