import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [45, 50, 55, 62, 68, 75, 82, 90]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["Study_Hours"].corr(df["Exam_Score"])

print("Correlation coefficient:", round(correlation, 2))

# Scatter plot
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()