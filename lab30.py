import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Patient dataset
# Features: Fever, Cough, Fatigue, Body_Pain
data = np.array([
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 1]
])

# Target: 0 = No condition, 1 = Condition
target = np.array([1, 1, 1, 0, 0, 0, 1, 0, 1, 0])

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(data)

# User inputs
fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
fatigue = int(input("Fatigue (0/1): "))
body_pain = int(input("Body Pain (0/1): "))

k = int(input("Enter value of k: "))

# Create KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Train model
model.fit(X, target)

# New patient
new_patient = [[fever, cough, fatigue, body_pain]]

# Scale new patient
new_patient = scaler.transform(new_patient)

# Prediction
prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("\nPrediction: Patient has the condition")
else:
    print("\nPrediction: Patient does not have the condition")