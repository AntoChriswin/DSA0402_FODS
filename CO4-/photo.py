# Question 7: Healthcare Treatment Cost Prediction Using Lasso Regression

# ---------------------------------------------------------
# 1. Import required libraries
# ---------------------------------------------------------
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ---------------------------------------------------------
# 2. Create the dataset
# ---------------------------------------------------------
data = {
    'Patient': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    'Age': [25, 35, 45, 55, 60, 30, 50, 40],
    'BP': [115, 125, 140, 155, 165, 120, 150, 135],
    'Sugar_Level': [90, 110, 150, 180, 200, 100, 170, 130],
    'BMI': [22, 25, 29, 32, 35, 24, 31, 27],
    'Previous_Visits': [1, 2, 3, 5, 6, 1, 4, 2],
    'Treatment_Cost': [5000, 8000, 15000, 25000, 32000, 7000, 22000, 12000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ---------------------------------------------------------
# 3. Identify input features and target variable
# ---------------------------------------------------------

# Input / Independent variables
X = df[['Age', 'BP', 'Sugar_Level', 'BMI', 'Previous_Visits']]

# Output / Dependent variable
y = df['Treatment_Cost']

print("\nInput Features:")
print(X.columns.tolist())

print("\nTarget Variable:")
print(y.name)


# ---------------------------------------------------------
# 4. Train-Test Split
# ---------------------------------------------------------

# 75% training and 25% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


# ---------------------------------------------------------
# 5. Feature Scaling
# ---------------------------------------------------------
# Scaling is important for Lasso because L1 regularization
# depends on the magnitude of the coefficients.

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ---------------------------------------------------------
# 6. Test different alpha values
# ---------------------------------------------------------

alpha_values = [0.1, 1.0, 10.0]

results = []

for alpha in alpha_values:

    # Create Lasso model
    model = Lasso(alpha=alpha, max_iter=10000)

    # Train model
    model.fit(X_train_scaled, y_train)

    # Predict test data
    y_pred = model.predict(X_test_scaled)

    # Evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    results.append([
        alpha,
        mae,
        mse,
        rmse,
        r2
    ])


# ---------------------------------------------------------
# 7. Display model comparison
# ---------------------------------------------------------

results_df = pd.DataFrame(
    results,
    columns=['Alpha', 'MAE', 'MSE', 'RMSE', 'R2 Score']
)

print("\nLasso Model Comparison:")
print(results_df.to_string(index=False))


# ---------------------------------------------------------
# 8. Select the best alpha
# ---------------------------------------------------------
# Highest R2 is considered better.

best_alpha = results_df.loc[
    results_df['R2 Score'].idxmax(),
    'Alpha'
]

print("\nBest Alpha:", best_alpha)


# ---------------------------------------------------------
# 9. Train final Lasso model using best alpha
# ---------------------------------------------------------

final_model = Lasso(
    alpha=best_alpha,
    max_iter=10000
)

final_model.fit(X_train_scaled, y_train)


# ---------------------------------------------------------
# 10. Predict treatment cost for test patients
# ---------------------------------------------------------

y_test_pred = final_model.predict(X_test_scaled)

prediction_df = X_test.copy()

prediction_df['Actual Cost'] = y_test.values
prediction_df['Predicted Cost'] = y_test_pred

print("\nTest Dataset Predictions:")
print(prediction_df)


# ---------------------------------------------------------
# 11. Evaluate final model
# ---------------------------------------------------------

mae = mean_absolute_error(y_test, y_test_pred)
mse = mean_squared_error(y_test, y_test_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_test_pred)

print("\nFinal Model Evaluation:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2 Score:", r2)


# ---------------------------------------------------------
# 12. Predict treatment cost for a new patient
# ---------------------------------------------------------

new_patient = pd.DataFrame({
    'Age': [48],
    'BP': [145],
    'Sugar_Level': [160],
    'BMI': [30],
    'Previous_Visits': [4]
})

# Scale new patient using the same scaler
new_patient_scaled = scaler.transform(new_patient)

# Prediction
new_prediction = final_model.predict(new_patient_scaled)

print("\nNew Patient:")
print(new_patient)

print("\nPredicted Treatment Cost for New Patient:")
print("₹", round(new_prediction[0], 2))


# ---------------------------------------------------------
# 13. Print Lasso coefficients
# ---------------------------------------------------------

coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': final_model.coef_
})

print("\nLasso Model Coefficients:")
print(coefficients)


# ---------------------------------------------------------
# 14. Identify important features
# ---------------------------------------------------------

print("\nFeature Importance Based on Lasso Coefficients:")

for feature, coefficient in zip(X.columns, final_model.coef_):

    if coefficient != 0:
        print(
            feature,
            "-> Important",
            "(Coefficient =", round(coefficient, 2), ")"
        )
    else:
        print(
            feature,
            "-> Removed by Lasso"
        )


# ---------------------------------------------------------
# 15. Final interpretation
# ---------------------------------------------------------

print("\nInterpretation:")
print("Lasso Regression uses L1 regularization to reduce")
print("the effect of less important features.")
print("Features with coefficients close to or equal to zero")
print("have less influence on treatment cost.")
print("Features with larger absolute coefficients have")
print("greater influence on the predicted treatment cost.")