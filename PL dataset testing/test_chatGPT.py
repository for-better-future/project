import numpy as np
import matplotlib.pyplot as plt

# Step 1: Dataset Creation (team data as a dictionary)
teams = np.array([
    ["Manchester City",38, 32, 4, 2, 94, 33],  # Example: Team Name, Wins, Losses, Draws, Goals Scored, Goals Against
    ["Arsenal", 38,26, 8, 4, 87, 42],
    ["Newcastle United",38, 19, 8, 11, 68, 43],
    ["Manchester United", 38, 20, 10, 8, 58, 40],
    ["Liverpool", 38, 18, 9, 11, 69, 47],
    ["Aston Villa",38, 18, 11, 9, 59, 47],
    ["Tottenham Hotspur", 38, 18, 13, 7, 63, 55],
    ["Brentford", 38, 14, 12, 12, 59, 46],
    ["Chelsea",38, 11, 13, 14, 38, 46],
    ["Brighton & Hove Albion",38, 15, 9, 14, 70, 53],
    ["Crystal Palace",38, 11, 14, 13, 40, 45],
    ["Wolverhampton Wanderers",38, 12, 15, 9, 40, 56],
    ["West Ham United",38, 12, 14, 10, 43, 51],
    ["Nottingham Forest",38, 9, 16, 13, 36, 63],
    ["Bournemouth",38, 9, 17, 12, 37, 71],
    ["Everton",38, 8, 19, 11, 34, 57],
    ["Sheffield United",38, 6, 23, 9, 32, 76],
    ["Burnley",38, 7, 23, 8, 30, 70],
    ["Luton Town",38, 5, 22, 11, 29, 67],
    ["Wolverhampton Wanderers",38, 12, 15, 9, 40, 56]
])

# Extract relevant data columns
team_names = teams[:, 0]
matches_played = teams[:, 1].astype(int)
wins = teams[:, 2].astype(int)
draws = teams[:, 3].astype(int)
losses = teams[:, 4].astype(int)
goals_scored = teams[:, 5].astype(int)
goals_conceded = teams[:, 6].astype(int)

# Step 2: Calculations using NumPy
points = wins * 3 + draws  # Points calculation: 3 points for a win, 1 for a draw
goal_difference = goals_scored - goals_conceded  # Goal difference: goals scored - goals conceded
total_goals = np.sum(goals_scored)  # Total goals scored by all teams
best_team_index = np.argmax(points)  # Team with the most points
best_goal_difference_index = np.argmax(goal_difference)  # Team with the best goal difference

# Print results
print(f"Total Goals Scored by All Teams: {total_goals}")
print(f"Team with the Most Points: {team_names[best_team_index]} with {points[best_team_index]} points")
print(f"Team with the Best Goal Difference: {team_names[best_goal_difference_index]} with {goal_difference[best_goal_difference_index]} goal difference")















# Step 3: Data Visualization using Matplotlib

# Bar Chart: Total Points of Each Team
plt.figure(figsize=(10, 6))
plt.barh(team_names, points, color='skyblue')
plt.xlabel('Points')
plt.ylabel('Teams')
plt.title('Premier League: Points by Team')
plt.gca().invert_yaxis()  # To display the highest points at the top
plt.show()

# Pie Chart: Distribution of Wins, Draws, and Losses
total_wins = np.sum(wins)
total_draws = np.sum(draws)
total_losses = np.sum(losses)

labels = ['Wins', 'Draws', 'Losses']
sizes = [total_wins, total_draws, total_losses]
colors = ['#4CAF50', '#FFEB3B', '#F44336']
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Premier League: Distribution of Wins, Draws, and Losses')
plt.show()

# Line Graph: Goals Scored by Each Team
plt.figure(figsize=(10, 6))
plt.plot(team_names, goals_scored, marker='o', linestyle='-', color='b')
plt.xlabel('Teams')
plt.ylabel('Goals Scored')
plt.title('Premier League: Goals Scored by Team')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
