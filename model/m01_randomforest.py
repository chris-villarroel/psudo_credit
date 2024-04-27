import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.metrics import precision_score
import joblib
import pickle


# 1. Read the CSV file
data = pd.read_csv('data/synthetic_loan_data.csv')


# 1.1 Filter data

data = data[['Debt_Burden', 'Employment_Years', 'Income', 'Loan_Amount', 'Age','Will_Default']]

# 2. Split the dataset into training and testing sets
X = data.drop('Will_Default', axis=1)  # Features
y = data['Will_Default']               # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# We'll need to convert categorical variables to numerical ones for the RandomForest
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

# 3. Create a RandomForest model and train it
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 4. Make predictions on the test set and generate a confusion matrix
y_pred = clf.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 5. Calculate the AUC and ROC
y_prob = clf.predict_proba(X_test)[:,1] # This will give you positive class prediction probabilities  
auc = roc_auc_score(y_test, y_prob)
print('AUC:', auc)

# Calculate precision
precision = precision_score(y_test, y_pred)
print('Precision:', precision)

# 6. Save the trained model
with open('data/random_forest_model.pkl', 'wb') as file:
    pickle.dump(clf, file)