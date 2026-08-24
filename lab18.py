import pandas as pd

# Post data
data = {
    "Post_ID": ["P01", "P02", "P03", "P04", "P05", "P06"],
    "Likes": [100, 200, 100, 300, 200, 100]
}

df = pd.DataFrame(data)

# Calculate frequency distribution
like_frequency = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(like_frequency)