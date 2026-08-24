import pandas as pd
import numpy as np
from scipy import stats

# Read CSV file
df = pd.read_csv("rare_elements.csv")

# User inputs
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired level of precision: "))

# Select sample
sample = df["Concentration"].dropna().sample(
    n=sample_size,
    random_state=42
)

# Point estimate
mean = np.mean(sample)

# Confidence level
confidence = confidence_level / 100

# Standard error
se = stats.sem(sample)

# Margin of error
t_value = stats.t.ppf(
    (1 + confidence) / 2,
    sample_size - 1
)

margin_error = t_value * se

# Confidence interval
lower = mean - margin_error
upper = mean + margin_error

print("\nPoint Estimate:", round(mean, 4))
print("Margin of Error:", round(margin_error, 4))
print(
    f"{confidence_level}% Confidence Interval:",
    (round(lower, 4), round(upper, 4))
)

# Check precision
if margin_error <= precision:
    print("Desired precision is achieved.")
else:
    print("Desired precision is not achieved.")