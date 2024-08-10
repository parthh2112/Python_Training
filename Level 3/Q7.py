def dict_using_for(student, subject):
    student_dict = {}
    for i in range(len(student)):
        student_dict[student[i]] = subject[i]
    return student_dict


def dict_comprehension(student, subject):
    return {students[i]: subjects[i] for i in range(len(students))}
         

students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

student_sub = dict_using_for(students, subjects)
print(student_sub)

student_subject = dict_comprehension(students, subjects)
print(student_subject)

