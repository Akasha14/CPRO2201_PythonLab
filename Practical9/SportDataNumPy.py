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

for i, avg in enumerate(average_points, start=1):
 print(f"Player {i}: {avg:.2f}")

# Task 3: Highest scorer per game.
highest_scores = np.max(scores, axis=0)

for i, score in enumerate(highest_scores, start=1):
    print(f"Game {i}: {score}")

# Task 4: Total points scored.
total_points = np.sum(scores, axis=1)

for i, total in enumerate(total_points, start=1):
    print(f"Player {i}: {total}")

# Task 5: Highest scorer.
total_points = np.sum(scores, axis=1)

# Find the player with the highest total points.
top_scorer = np.argmax(total_points)

# Print the result
print(f"Top scorer: Player {top_scorer + 1}")