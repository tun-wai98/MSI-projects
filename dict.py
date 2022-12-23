student_dictionary = {"Steve Allen":30, "Michael Smith":80, "Jhon Paul":40, "James Henry":60}

passed_students_names = []

for a, b in student_dictionary.items():
    if b >= 50:
        passed_students_names.append(a)


print([a.split()[0] for a in passed_students_names])

#sayar's answers
student_dictionary = {"Steve Allen":30, "Michael Smith":80, "Jhon Paul":40, "James Henry":60}

passed_students_names = [name.split()[0] for name, grade in student_dictionary.items() if grade > 50]
print(passed_students_names)