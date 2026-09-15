from collections import Counter
import re

# Open and read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Convert text to lowercase
text = text.lower()

# Extract words and remove punctuation
words = re.findall(r'\b\w+\b', text)

# Count the frequency of each word
word_frequency = Counter(words)

# Display the frequency distribution
print("Word Frequency Distribution:")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)
