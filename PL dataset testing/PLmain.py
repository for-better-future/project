import numpy as np
import matplotlib.pyplot as plt

print("This is the PL season 2072-73:")

# Step 1: Dataset Creation (team data as a dictionary)
teams = np.array([
    ["Manchester City", 38, 32, 4, 2, 94, 33], 
    ["Arsenal", 38, 26, 8, 4, 87, 42],
    ["Newcastle United", 38, 19, 8, 11, 68, 43],
    ["Manchester United", 38, 20, 9, 9, 58, 40],
    ["Liverpool", 38, 18, 9, 11, 69, 47],
    ["Aston Villa", 38, 18, 11, 9, 59, 47],
    ["Tottenham Hotspur", 38, 18, 12, 8, 63, 55],
    ["Brentford", 38, 14, 12, 12, 59, 46],
    ["Chelsea", 38, 11, 13, 14, 38, 46],
    ["Brighton & Hove Albion", 38, 15, 9, 14, 70, 53],
    ["Crystal Palace", 38, 11, 14, 13, 40, 45],
    ["Wolverhampton Wanderers", 38, 12, 15, 9, 40, 56],
    ["West Ham United", 38, 12, 14, 10, 43, 51],
    ["Nottingham Forest", 38, 9, 16, 13, 36, 63],
    ["Bournemouth", 38, 9, 17, 12, 37, 71],
    ["Everton", 38, 8, 19, 11, 34, 57],
    ["Sheffield United", 38, 6, 23, 9, 32, 76],
    ["Burnley", 38, 7, 23, 8, 30, 70],
    ["Luton Town", 38, 5, 21, 12, 29, 67],
    ["Leeds United",38, 8, 16, 14, 40, 56]
])

team_names1 = teams[:, 0]
matches_played1 = teams[:, 1].astype(int)
wins1 = teams[:, 2].astype(int)
draws1 = teams[:, 3].astype(int)
losses1 = teams[:, 4].astype(int)
goals_scored1 = teams[:, 5].astype(int)
goals_conceded1 = teams[:, 6].astype(int)


# Step 2: Calculations using NumPy
points = wins1 * 3 + draws1 
np.argsort(points)
print(points)


goal_difference = goals_scored1 - goals_conceded1  # Goal difference: goals scored - goals conceded
max_points=np.argmax(points)
# Step 3: Sort teams by points in descending order

sorted_indices = np.argsort(points)[::-1]  # Sort indices by points (descending)
sorted_teams = teams[sorted_indices]  # Sorted teams based on points

team_names = sorted_teams[:, 0]
matches_played = sorted_teams[:, 1].astype(int)
wins = sorted_teams[:, 2].astype(int)
draws = sorted_teams[:, 3].astype(int)
losses = sorted_teams[:, 4].astype(int)
goals_scored = sorted_teams[:, 5].astype(int)
goals_conceded = sorted_teams[:, 6].astype(int)



top_four_teams=sorted_teams[:4]
sorted_indices# Sort indices by points (descending)
print(sorted_teams)

print(f"The winner of the PLseason2072-73\n{team_names[max_points]} with the points of {points[max_points]}")
print("\n")
print("what data you want to see:\n")
print("for top four: 1\n")
print("relegated teams: 2\n")
print("europa league teams: 3\n")
print("conference league: 4\n")
count=1
while count>2:
 task=int(input(":"))
 if task == 1:
     print("The top four teams are:\n")
     print(f"The First team:\n{team_names[:1]} with the points of {points[:1]}")
     print("")
     print(f"The second team:\n{team_names[1:2]} with the points of {points[1:2]}")
     print("")
     print(f"The Third team:\n{team_names[2:3]} with the points of {points[3:4]}")
     print("")
     print(f"The Fourth team:\n{team_names[3:4]} with the points of {points[2:3]}")
     print("")


 elif task==2:
     relegated=sorted_teams[-3:]
     for i,team in enumerate(relegated,start=1):
         print(f"The {i} teams: {team[0]} with {points[sorted_indices[-3 + i - 1]]} points")
  
 elif task==3:
     europa_league=sorted_teams[5:7]
     for i,team in enumerate(europa_league,start=1):
         print(f"Then {i} team: {team[0]} with {points[sorted_indices[5 + i -1]]}") 

 elif task ==4:
      confernce_league=sorted_teams[6:7]
      for i,team in enumerate(confernce_league,start=1):
          print(f"The {i} team: {team[0]} with {points[sorted_indices[6 + i - 1]]} points")

 else:
      print("plz enter the correct value")

 con=input("you want to continue y/n\n")
 if con=="y":
   continue
 if con=="n":
            i=3
 if con!="y" and  con!="n":
     print("invalid input task got terminated")
     break



x_axis  =   team_names
y_axis  =    points[sorted_indices]

plt.bar(x_axis, y_axis, color='skyblue', edgecolor='black')
plt.xlabel("Teams")
plt.ylabel("Points")
plt.title("Premier League 2072-73: Team Points")

plt.xticks(rotation=90)  # Rotate team names for better visibility
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Create a figure with 2 subplots (1 row, 2 columns)
fig, axes   =   plt.subplots(1, 2, figsize=(10, 5))

# First subplot
axes[0].bar(team_names,goals_scored , color='skyblue', edgecolor='black')
axes[0].set_title('Goal Scored by all Teams')
axes[0].set_xlabel('Teams')
axes[0].set_ylabel('Goaks')
axes[0].tick_params(axis='x', rotation=90)  
# Second subplot
axes[1].bar(team_names,goals_conceded , color='lightgreen', edgecolor='black')
axes[1].set_title('Goal Conceded by all Teams')
axes[1].set_xlabel('Teams')
axes[1].set_ylabel('Goals conceded')
plt.xticks(rotation=90)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.xticks(rotation=90)
# Display the plots
plt.show()


#pie chart for relegated teams
plt.figure(figsize=(8, 6))

values = [10, 10, 10, 10, 10,
          10, 10, 10, 10, 10,
          10, 10, 10, 10, 10,
          10, 10, 20, 20, 20
          ]  # Equal values for all categories
explode = [0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 
           0, 0, 0.1, 0.1, 0.1,]  # Slightly explode all slices
colors=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']
plt.pie(values,colors=colors, startangle=90, explode=explode)

plt.legend(team_names, loc="center left", bbox_to_anchor=(1, 0.5), title="TEAMS")
plt.title("Relegated Teams")
plt.tight_layout()
plt.show()