# Example data
data = [
    ("Alice", [14, 16, 18]),
    ("Bob", [12, 9, 10]),
    ("Charlie", [19, 20, 17]),
    ("Diana", [8, 7, 10])
]

# Initializing variables
count = 0 
students = []
max_score = 0

# Iterate through the data
for name, scores in data:
    average = sum(scores) / len(scores)  # Calculate the average once

    # Check if there's at least one score < 10 (counting unique students)
    if any(score < 10 for score in scores):
        count += 1

    # Add student if average is >= 15
    if average >= 15:
        students.append((name, round(average)))

    # Track highest score directly in the same loop
    max_score = max(max_score, *scores)

# Display results
print(f"Students with an average score greater than or equal to 15: {students}")
print(f"Count of students that have at least one score under 10: {count}")
print(f"Highest individual score: {max_score}")
