import numpy as np
from scipy.stats import ttest_ind

# Conversion rates for website A and B
A = np.array([
    0.12, 0.15, 0.11, 0.14, 0.13,
    0.16, 0.12, 0.15, 0.14, 0.13
])

B = np.array([
    0.18, 0.20, 0.17, 0.19, 0.21,
    0.18, 0.20, 0.19, 0.22, 0.18
])

# Independent t-test
t_stat, p_value = ttest_ind(A, B)

print("Mean Conversion Rate - A:", round(A.mean(), 3))
print("Mean Conversion Rate - B:", round(B.mean(), 3))
print("t-statistic:", round(t_stat, 3))
print("p-value:", round(p_value, 4))

# Hypothesis test
alpha = 0.05

if p_value < alpha:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")