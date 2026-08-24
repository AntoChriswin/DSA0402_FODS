import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

# Load CSV file
df = pd.read_csv("data.csv")

# Stop words
stop_words = {
    "the", "and", "is", "a", "an", "of",
    "to", "in", "for", "on", "this", "that",
    "it", "was", "with", "very", "are"
}

# Combine all feedback
text = " ".join(df["feedback"].astype(str))

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r'[^a-zA-Z\s]', '', text)

# Split into words
words = text.split()

# Remove stop words
words = [word for word in words if word not in stop_words]

# Calculate frequency distribution
frequency = Counter(words)

# Get N from user
N = int(input("Enter the number of top words to display: "))

# Get top N words
top_words = frequency.most_common(N)

print("\nTop", N, "Most Frequent Words:")

for word, count in top_words:
    print(word, ":", count)

# Prepare data for plotting
words_list = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

# Create bar graph
plt.bar(words_list, counts)

plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()