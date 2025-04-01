import numpy as np

# Task 1: Create 2D NumPy array.
scores = np.array([
    [10, 15, 13, 18],  # Player 1.
    [8, 12, 14, 16],   # Player 2.
    [5, 7, 9, 10],     # Player 3.
    [14, 18, 17, 20],  # Player 4.
    [20, 22, 19, 25]   # Player 5.
])

# Task 2: Average points per game.
average_points = np.mean(scores, axis=1)

print("Average points per game for each player:")
for i, avg in enumerate(average_points, start=1):
 print(f"Player {i}: {avg:.2f}")

# Task 3: Highest scorer per game.
highest_scores = np.max(scores, axis=0)

print("\nHighest scorer in each game:")
for i, score in enumerate(highest_scores, start=1):
    print(f"Game {i}: {score}")

# Task 4: Total points scored.

total_points = np.sum(scores, axis=1)

print("\nTotal points scored by each player:")
for i, total in enumerate(total_points, start=1):
    print(f"Player {i}: {total}")

# Task 5: Top scorer.
# Find the player with the highest total points.
top_scorer = np.argmax(total_points)

# Print the result
print(f"\nTop scorer: Player {top_scorer + 1}")

# Task 6: Worst Performance.
min_scores = np.min(scores, axis=1)

# Find the player with the lowest total points.
worst_player = np.argmin(min_scores)

print(f"\nPlayer with the worst performance: Player {worst_player + 1}")

# Task 7: Compare player 1 and 2.
# Slice to get scores.
player_1 = scores[0, :]  # All scores of Player 1.
player_2 = scores[1, :]  # All scores of Player 2.

# Calculate the difference for each game.
performance_difference = player_1 - player_2

print("\nDifference in performance between player 1 and 2 in each game:")
for i, diff in enumerate(performance_difference, start=1):
    print(f"Game {i}: {diff} points")

# Task 8: Difference in total points between player 4 and 5.
player_4_points = np.sum(scores[3, :])  # Total for Player 4.
player_5_points = np.sum(scores[4, :])  # Total for Player 5.

# Calculate the difference in total points
difference = player_4_points - player_5_points

# Print the result
print(f"\nDifference in total points between Player 4 and Player 5: {difference}")