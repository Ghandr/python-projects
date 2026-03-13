def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def assign_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students in the class: "))

students = []

# For each student, prompt the user to enter their name and three test scores
for _ in range(num_students):
    name = input("Enter the student's name: ")
    score1 = float(input("Enter the first test score: "))
    score2 = float(input("Enter the second test score: "))
    score3 = float(input("Enter the third test score: "))
    
    average = calculate_average(score1, score2, score3)
    grade = assign_grade(average)
    
    students.append({
        "name": name,
        "average": average,
        "grade": grade
    })

# Print the results for each student
for student in students:
    print(f"Name: {student['name']}, Average Score: {student['average']:.2f}, Grade: {student['grade']}")





