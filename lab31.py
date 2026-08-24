import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Create patient dataset
data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 28, 32,
            38, 42, 48, 52, 58, 62, 27, 34, 46, 56],

    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F",
               "F", "M", "F", "M", "F", "M", "F", "M",
               "M", "F", "M", "F"],

    "Blood_Pressure": [120, 125, 130, 135, 140, 145, 150, 155,
                       118, 128, 132, 138, 142, 148, 152, 158,
                       122, 126, 136, 146],

    "Cholesterol": [180, 190, 200, 210, 220, 230, 240, 250,
                    175, 195, 205, 215, 225, 235, 245, 255,
                    185, 198, 212, 228],

    "Outcome": ["Good", "Good", "Good", "Good", "Good",
                "Bad", "Bad", "Bad", "Good", "Good",
                "Good", "Good", "Bad", "Bad", "Bad",
                "Bad", "Good", "Good", "Bad", "Bad"]
}

df = pd.DataFrame(data)

# Encode Gender
gender_encoder = LabelEncoder()
df["Gender"] = gender_encoder.fit_transform(df["Gender"])

# Encode target
outcome_encoder = LabelEncoder()
df["Outcome"] = outcome_encoder.fit_transform(df["Outcome"])

# Features and target
X = df[["Age", "Gender", "Blood_Pressure", "Cholesterol"]]
y = df["Outcome"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Standardize features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Train model
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

# Display metrics
print("KNN Model Performance")
print("----------------------")
print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1-Score :", round(f1 * 100, 2), "%")

# Display predictions
results = pd.DataFrame({
    "Actual": outcome_encoder.inverse_transform(y_test),
    "Predicted": outcome_encoder.inverse_transform(y_pred)
})

print("\nTest Set Predictions:")
print(results.to_string(index=False))