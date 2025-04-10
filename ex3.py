# Exercice 3 : Correction et Optimisation avec Listes et Tuples
# Example data
data = [
    ("Alice", [14, 16, 18]),
    ("Bob", [12, 9, 10]),
    ("Charlie", [19, 20, 17]),
    ("Diana", [8, 7, 10])
]
# 1. Display the average score of each student where the average is greater than or equal to 15
# 2 figuring out the maximum average score among all students
max = 0 
count = 0 
students = []
for dot in data :
    test = True
    average = 0 
    name, scores = dot
    for score in scores :
        # 3 : If the score is less than 10, set test to False and count the number of students that have at least one score less than 10 
        if score <10 and test == True: 
            test = False
            count += 1
        average += score
    # ...........
    if average >= 15 :
        if(max < average) :
            max = average
        students.append((name , round(average/len(scores))))


#  Display the highest individual score among all students    
print(f"Students with an average score greater than or equal to 15:{students}")
print(f"Count of students that have at least one score under 10 : {count}")
print(f"Highest student score : {max}")