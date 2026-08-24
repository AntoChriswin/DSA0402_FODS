import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Treatment group
treatment = np.array([
    82, 85, 80, 88, 84, 86, 83, 87, 81, 85
])

# Control / placebo group
control = np.array([
    75, 78, 74, 77, 76, 73, 79, 75, 77, 74
])

# Perform independent t-test
t_stat, p_value = ttest_ind(treatment, control)

print("Treatment Mean:", round(treatment.mean(), 2))
print("Control Mean:", round(control.mean(), 2))
print("t-statistic:", round(t_stat, 3))
print("p-value:", round(p_value, 4))

# Hypothesis decision
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("The treatment has a statistically significant effect.")
else:
    print("Fail to reject the null hypothesis.")
    print("The treatment does not have a statistically significant effect.")

# Visualize the groups
groups = ["Control", "Treatment"]
means = [control.mean(), treatment.mean()]

plt.bar(groups, means)
plt.title("Treatment vs Control")
plt.xlabel("Group")
plt.ylabel("Mean Measurement")
plt.show()