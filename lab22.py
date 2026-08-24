import numpy as np
from scipy import stats

# Blood pressure reduction data for 25 patients in each group
drug = np.array([
    12, 15, 10, 14, 13, 16, 11, 15, 12, 14,
    13, 17, 10, 16, 14, 12, 15, 13, 11, 14,
    16, 12, 13, 15, 14
])

placebo = np.array([
    5, 7, 4, 6, 8, 5, 6, 7, 4, 5,
    6, 8, 5, 7, 6, 4, 5, 6, 7, 5,
    6, 4, 7, 5, 6
])

# 95% Confidence Interval
drug_ci = stats.t.interval(
    0.95,
    len(drug) - 1,
    loc=np.mean(drug),
    scale=stats.sem(drug)
)

placebo_ci = stats.t.interval(
    0.95,
    len(placebo) - 1,
    loc=np.mean(placebo),
    scale=stats.sem(placebo)
)

print("Drug Group")
print("Mean reduction:", round(np.mean(drug), 2))
print("95% Confidence Interval:", 
      (round(drug_ci[0], 2), round(drug_ci[1], 2)))

print("\nPlacebo Group")
print("Mean reduction:", round(np.mean(placebo), 2))
print("95% Confidence Interval:",
      (round(placebo_ci[0], 2), round(placebo_ci[1], 2)))