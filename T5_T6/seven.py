students = ["Smit", "Jaya", "Rayyan"]
subjects = ["CSE", "Networking", "Operating System"]
student_subject = {}
for student, subject in zip(students, subjects):
    student_subject[student] = subject

print(student_subject)
