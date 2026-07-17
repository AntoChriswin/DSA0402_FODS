import numpy as np

# 4x4 matrix (Rows = Students, Columns = Math, Science, English, History)
student_scores = np.array([
    [85, 78, 90, 88],
    [92, 81, 87, 85],
    [76, 89, 84, 91],
    [88, 85, 91, 86]
])

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Calculate average score for each subject (column-wise)
average_scores = np.mean(student_scores, axis=0)

# Find the subject with the highest average
highest_avg_index = np.argmax(average_scores)

# Display results
print("Average score for each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

print("\nSubject with the highest average score:", subjects[highest_avg_index])
print("Highest Average Score:", average_scores[highest_avg_index])