# Dictionary to map letter grades to their corresponding grade points
grade_point_mapping = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

# Initialize variables to keep track of total grade points and the number of grades entered
total_grade_points = 0.0
num_grades = 0

# Continuously prompt the user for letter grades until they enter a blank line
while True:
    grade = input("Enter a letter grade (or leave blank to finish): ").strip().upper()

    if grade == "":
        break  # User entered a blank line, exit the loop
    elif grade in grade_point_mapping:
        grade_points = grade_point_mapping[grade]
        total_grade_points += grade_points
        num_grades += 1
    else:
        print("Invalid grade. Please enter a valid letter grade.")

# Calculate the GPA
if num_grades > 0:
    gpa = total_grade_points / num_grades
    print(f"Grade Point Average (GPA): {gpa:.2f}")
else:
    print("No grades entered. GPA cannot be calculated.")
