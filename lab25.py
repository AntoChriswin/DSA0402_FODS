import pandas as pd
from scipy import stats

# Read customer reviews
df = pd.read_csv("customer_reviews.csv")

ratings = df["Rating"].dropna()

# Calculate mean
mean_rating = ratings.mean()

# Calculate standard error
standard_error = stats.sem(ratings)

# 95% confidence interval
confidence_interval = stats.t.interval(
    0.95,
    len(ratings) - 1,
    loc=mean_rating,
    scale=standard_error
)

print("Number of Reviews:", len(ratings))
print("Mean Rating:", round(mean_rating, 2))

print(
    "95% Confidence Interval:",
    (round(confidence_interval[0], 2),
     round(confidence_interval[1], 2))
)