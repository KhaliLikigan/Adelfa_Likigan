scores = []

for i in range(5):
    scores.append(int(input(f"Enter Quiz {i+1} Score:" )))

print(f"Quiz Scores: {scores}")

print(f"Number of Quizzes: {len(scores)}")

total = sum(scores)
print(f"Total Score: {total}")

average = total / len(scores)
print(f"Average Score: {average:.2f}")

print(f"Highest Score: {max(scores)}")

print(f"Lowest Score: {min(scores)}")

scores.sort()
print(f"Ascending: {scores}")

scores.reverse()
print(f"Descending: {scores}")

print(f"Original Scores: {scores}")