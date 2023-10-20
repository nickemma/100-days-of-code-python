# def invert_courses_dict(student_courses):
#     inverted_dict = {}
#   # Iterate through the original dictionary
#     for student, courses in student_courses.items():
#       # Iterate through the list of courses for each student
#       for course in courses:
#           if course in inverted_dict:
#               inverted_dict[course].append(student)
#           else:
#               inverted_dict[course] = [student]

#     return inverted_dict

# # Sample input dictionary
# student_courses = {
#     'Stud1': ['CS1101', 'CS2402', 'CS2001'],
#     'Stud2': ['CS2402', 'CS2001', 'CS1102']
# }

# # Invert the dictionary
# inverted_output = invert_courses_dict(student_courses)
# # Print the original and inverted dictionaries
# print("Original Dictionary:")
# print(student_courses)
# print("\nInverted Dictionary:")
# print(inverted_output)

# Looping over two lists with zip function

students = ['Emmanuel', 'Jessica', 'Julius']
student_grade = [90, 80, 70]

for student, grade in zip(students, student_grade, strict=True):
    print(f"{student} got {grade}%")


programming_languages = ["Python", "Java", "Golang", "Javascript"]

for index, programming in enumerate(programming_languages):
    print(f"The programming language at index {index}: is {programming}")


employee_salaries = {
    "Emmanuel": 60000,
    "Jessica": 55000,
    "Julius": 62000
}

for name, salary in employee_salaries.items():
    print(f"{name} has a salary of {salary}.")
