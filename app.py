from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('data/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict_get', methods=['GET'])
def predict_get():
    try:
        # Extract and cast values from the GET request
        debt_burden = float(request.args.get('Debt_Burden'))
        employment_years = int(request.args.get('Employment_Years'))
        income = int(request.args.get('Income'))
        loan_amount = int(request.args.get('Loan_Amount'))
        age = int(request.args.get('Age'))

        # Create DataFrame for the model input
        data = pd.DataFrame([[debt_burden, employment_years, income, loan_amount, age]],
                            columns=['Debt_Burden', 'Employment_Years', 'Income', 'Loan_Amount', 'Age'])

        # Make predictions
        prediction = model.predict(data)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return str(e)

@app.route('/predict_post', methods=['POST'])
def predict_post():
    try:
        # Extract values from the POST request JSON body
        data = request.get_json()

        # Cast data to the appropriate data types
        data = {
            'Debt_Burden': float(data['Debt_Burden']),
            'Employment_Years': int(data['Employment_Years']),
            'Income': int(data['Income']),
            'Loan_Amount': int(data['Loan_Amount']),
            'Age': int(data['Age'])
        }
        
        # Convert to DataFrame
        input_data = pd.DataFrame([data.values()], columns=data.keys())

        # Make predictions
        prediction = model.predict(input_data)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
