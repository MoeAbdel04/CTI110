# CTI-110
# P2HW2: List
# Mahamed Abdel
# 10/13/23

# Initialize variables for total grades and count of modules
# Create an empty list to store grades
# Start a loop to input grades for 6 modules 
# Prompt the user to enter the grade for the current module
# Add the grade to the list of grades
# Update the total grades and module count
# Calculate the lowest, highest, and average grades
# Display the results





grades = []
for module in range(1, 7):
    grade = float(input(f"Enter grade for Module {module}: "))
    grades.append(grade)

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\nGrade Summary:")
print(f"Lowest Grade: {lowest:.2f}")
print(f"Highest Grade: {highest:.2f}")
print(f"Sum of Grades: {total:.2f}")
print(f"Grades Average: {average:.2f}")
