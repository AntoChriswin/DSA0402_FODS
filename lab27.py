import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland",
             "Salah", "De Bruyne", "Kane", "Vinicius", "Bellingham"],
    "Age": [36, 39, 32, 25, 24, 32, 33, 31, 23, 20],
    "Position": ["Forward", "Forward", "Forward", "Forward", "Forward",
                 "Forward", "Midfielder", "Forward", "Forward", "Midfielder"],
    "Goals": [25, 22, 18, 30, 28, 20, 12, 24, 19, 15],
    "Weekly_Salary": [1200000, 1100000, 900000, 1000000, 950000,
                      700000, 600000, 650000, 500000, 450000]
}

df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("soccer_players.csv", index=False)

# Read CSV file
players = pd.read_csv("soccer_players.csv")

print("Dataset:")
print(players)

# Top 5 players by goals
top_goals = players.sort_values("Goals", ascending=False).head(5)

print("\nTop 5 Players by Goals:")
print(top_goals[["Name", "Goals"]])

# Top 5 players by salary
top_salary = players.sort_values("Weekly_Salary", ascending=False).head(5)

print("\nTop 5 Players by Salary:")
print(top_salary[["Name", "Weekly_Salary"]])

# Average age
average_age = players["Age"].mean()

print("\nAverage Age:", round(average_age, 2))

# Players above average age
above_average = players[players["Age"] > average_age]

print("\nPlayers Above Average Age:")
print(above_average[["Name", "Age"]])

# Position distribution
position_count = players["Position"].value_counts()

print("\nPlayers by Position:")
print(position_count)

# Bar chart
position_count.plot(kind="bar")

plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.xticks(rotation=0)
plt.show()