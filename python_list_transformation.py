# Task 1: Given the list of grades:
# Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]     

grades.sort()
grades.reverse()
print(f"the grades (desc): {grades}")

# Task 2: Calculate the average grade and print it.
count = 0
for grade in grades:
    count += grade
average_grade = count / len(grades)

print(f"The average grade is {average_grade}")