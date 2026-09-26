# 💰 Pocket Smart – Smart Budget Recommendation Assistant

Pocket Smart is a beginner-friendly personal budgeting application built with **Python and Streamlit**.

It accepts a user's monthly income, expenses, savings goal, and risk preference, then produces a simple budget recommendation.

## Features

- Monthly income and expense input
- Savings-goal based recommendation
- Monthly surplus calculation
- Recommended savings amount
- Flexible spending amount
- Emergency-fund target
- Risk-preference guidance
- Visual budget breakdown
- Simple, responsive Streamlit interface

## Tech Stack

- Python
- Streamlit
- Pandas
- GitHub
- Streamlit Community Cloud (deployment)

## Project Structure

```text
pocket-smart/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── sample_budget.csv
```

## Run Locally

### 1. Install Python

Use Python 3.10 or newer.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
streamlit run app.py
```

The browser will open the Pocket Smart application.

## Deploy with GitHub + Streamlit Community Cloud

1. Create a new GitHub repository named `pocket-smart`.
2. Upload all project files.
3. Open Streamlit Community Cloud.
4. Connect your GitHub account.
5. Select the `pocket-smart` repository.
6. Select `app.py` as the main file.
7. Click **Deploy**.

Streamlit will install the packages listed in `requirements.txt` and start the app.

## How the Recommendation Works

The first version uses a transparent rule-based budgeting model:

- Monthly surplus = Income − Expenses
- A target savings amount is calculated using approximately 20% of income and the user's savings goal.
- Recommended savings cannot exceed the current monthly surplus.
- The remaining surplus becomes flexible spending.
- Emergency-fund target = approximately 3 months of income.

This is an educational prototype, not professional financial advice.

## Future Improvements

- Expense-category tracking
- Login/user profiles
- SQLite or PostgreSQL database
- AI-powered spending insights
- CSV expense upload
- Monthly budget history
- Charts and dashboards
- Personalized alerts
- Multi-language support
- Authentication
- Cloud database integration

## License

For educational/project use.
