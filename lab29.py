from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create Decision Tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X, y)

# Get user input
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Create input data
new_flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

# Predict species
prediction = model.predict(new_flower)

print("\nPredicted Iris Species:",
      iris.target_names[prediction[0]])