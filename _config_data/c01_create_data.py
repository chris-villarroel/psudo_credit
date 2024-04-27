import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Number of instances
n = 10000

# Generate attributes

# For simplicity, some attributes are randomly generated within a reasonable range or selected from a list

client_ids = ["cliente_id_{}".format(i) for i in range(1, n+1)]
credit_history = np.random.choice(['Excellent', 'Good', 'Fair', 'Poor'], n)
debt_burden = np.random.uniform(0.1, 1.5, n)  # Randomly generate debt-to-income ratio between 0.1 and 1.5
employment_years = np.random.randint(0, 20, n)  # Randomly generate employment years between 0 to 20
income = np.random.randint(20000, 200000, n)  # Randomly generate annual income between $20,000 and $200,000
loan_amount = np.random.randint(50000, 500000, n)  # Randomly generate loan amounts
down_payment = income * 0.2 + np.random.randn(n)*5000  # A random 20% of income +/- noise
LTV = (loan_amount - down_payment) / loan_amount
property_type = np.random.choice(['Primary Residence', 'Rental', 'Vacation Home'], n)
savings = np.random.uniform(0, 50000, n)  # Random savings between 0 and $50,000
interest_rate_type = np.random.choice(['Fixed', 'Variable'], n)
marital_status = np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], n)
age = np.random.randint(20, 70, n)
education = np.random.choice(['High School', 'Bachelor', 'Masters', 'PhD'], n)
location = np.random.choice(['Urban', 'Suburban', 'Rural'], n)
recent_credit_activity = np.random.choice(['Low', 'Moderate', 'High'], n)

# Simple method to generate whether a user will default based on some conditions

def will_default(credit, debt, employment_years, income, savings, LTV, loan_amount, property_type, age, recent_credit_activity):
    risk = 0

    # Credit history related risks
    if credit == 'Poor':
        risk += 3
    elif credit == 'Fair':
        risk += 1

    # Debt and financial stability related risks
    if debt > 1.2:
        risk += 2
    if income < 30000:
        if savings < 5000:
            risk += 2
        else:
            risk += 1
    if LTV > 0.9:
        risk += 2
    elif LTV > 0.8:
        risk += 1

    # Employment related risks
    if employment_years < 2:
        risk += 1

    # Loan amount related risks
    if loan_amount > 400000:
        risk += 1

    # Property type related risks
    if property_type == 'Rental':
        risk += 1

    # Age related risks (young borrowers might be seen as more risky due to less credit history)
    if age < 25:
        risk += 1

    # Recent credit activity risks
    if recent_credit_activity == 'High':
        risk += 1

    # Introduce some randomness
    random_factor = np.random.uniform(-3, 2)  # A random number between 0 and 2

    # Summing up the risks
    if risk + random_factor > 7:  # The threshold of 7 is chosen arbitrarily. Adjust as needed.
        return 1

    return 0

defaults = np.array([will_default(credit, debt, employ_years, inc, sav, ltv, loan_amt, prop_type, age_val, recent_credit) 
                     for credit, debt, employ_years, inc, sav, ltv, loan_amt, prop_type, age_val, recent_credit in 
                     zip(credit_history, debt_burden, employment_years, income, savings, LTV, loan_amount, property_type, age, recent_credit_activity)])


# Compile data into a pandas DataFrame
data = pd.DataFrame({
    #'Client_ID': client_ids,
    'Credit_History': credit_history,
    'Debt_Burden': debt_burden,
    'Employment_Years': employment_years,
    'Income': income,
    'Loan_Amount': loan_amount,
    'Down_Payment': down_payment,
    'LTV': LTV,
    'Property_Type': property_type,
    'Savings': savings,
    'Interest_Rate_Type': interest_rate_type,
    'Marital_Status': marital_status,
    'Age': age,
    'Education': education,
    'Location': location,
    'Recent_Credit_Activity': recent_credit_activity,
    'Will_Default': defaults
})

print(data.head())

print(data['Will_Default'].value_counts())

data.to_csv('data/synthetic_loan_data.csv', index=False)
