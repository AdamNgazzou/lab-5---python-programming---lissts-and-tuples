# 🧪 Python Lab – Lists, Tuples & Code Optimization Using Built-in Functions

---

## ✅ Exercise 1: Working with Lists

**Objective**: Create and manipulate a list of students.

**Instructions**:  
A professor wants to manage the list of students enrolled in a course. Write a Python program that performs the following steps:

1. Ask the user for the number of students to register.
2. For each student, ask for their name and add it to a list.
3. Display the complete list of students.
4. Display the list sorted in alphabetical order.
5. Display the total number of students.
6. Ask the user for a name to remove from the list. If it exists, remove it and display the updated list.

---

## ✅ Exercise 2: Working with Tuples

**Objective**: Practice storing and processing geographical coordinates using tuples.

**Instructions**:  
Write a Python program to manage geographical coordinates stored as `(latitude, longitude)` tuples.

1. Create a list of 3 tuples, each representing a city:
   - Paris: (48.8566, 2.3522)  
   - New York: (40.7128, -74.0060)  
   - Tokyo: (35.6895, 139.6917)
2. Display each city along with its coordinates.
3. Use a loop to display only the **latitude** of each city.
4. Compute and display the **average latitude** of all 3 cities.

---

## ✅ Exercise 3: Code Fixing and Optimization with Lists & Tuples

**Objective**: Analyze a poorly written code snippet that uses lists and tuples, and optimize it using **built-in Python functions**, **list comprehensions**, and **good practices**.

**Instructions**:  
You are given a list of tuples. Each tuple contains:

- A name (`str`)
- A list of integers representing scores for different tasks.

```
# Example data
data = [
    ("Alice", [14, 16, 18]),
    ("Bob", [12, 9, 10]),
    ("Charlie", [19, 20, 17]),
    ("Diana", [8, 7, 10])
]
```

Your task is to:

1. Identify students whose **average score is >= 15**.
2. Display a list of names of these students.
3. Display the **highest individual score** among **all** students.
4. Count how many students have at least one score **below 10**.
5. Rewrite and optimize the following **inefficient code** that performs a similar task:

```
# Poorly written and repetitive code
data = [("Alice", [14, 16, 18]), ("Bob", [12, 9, 10]), ("Charlie", [19, 20, 17]), ("Diana", [8, 7, 10])]
selected = []
high = 0
count = 0

for i in range(len(data)):
    total = 0
    for j in range(len(data[i][1])):
        score = data[i][1][j]
        total += score
        if score > high:
            high = score
        if score < 10:
            count += 1
            break
    average = total / len(data[i][1])
    if average >= 15:
        selected.append(data[i][0])

print("Selected students:", selected)
print("Highest score:", high)
print("Students with at least one score < 10:", count)
```

---

### 🔧 **Expected Output**:
```
Selected students: ['Alice', 'Charlie']
Highest score: 20
Students with at least one score < 10: 2
```