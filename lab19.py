import pandas as pd
from collections import Counter
import re

# Customer reviews
data = {
    "Review": [
        "Good product and good quality",
        "Excellent product and good service",
        "Good quality and excellent service"
    ]
}

df = pd.DataFrame(data)

# Combine all reviews
text = " ".join(df["Review"])

# Convert to lowercase
text = text.lower()

# Extract words
words = re.findall(r'\b\w+\b', text)

# Calculate frequency
frequency = Counter(words)

print("Word Frequency Distribution:")

for word, count in frequency.most_common():
    print(word, ":", count)