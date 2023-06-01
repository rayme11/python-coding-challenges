# Write a function called get_highest_grade that takes a dictionary student_grades as input.
# The dictionary contains student names as keys and their corresponding grades as values.
# However, each student's grade is represented by a nested dictionary, ' \
# 'where the subject is the key and the grade is the value. ' \
#                      'Your task is to find and return the highest grade among all the students.
#
#
# Example:
#
#
# student_grades = {
#     "Alice": {
#         "Math": 95,
#         "Science": 87,
#         "History": 92
#     },
#     "Bob": {
#         "Math": 88,
#         "Science": 91,
#         "History": 90
#     },
#     "Charlie": {
#         "Math": 75,
#         "Science": 82,
#         "History": 78
#     }
# }

def get_highest_grade(grades):
    list_grades = []
    for student, grades in grades.items():
        # print('\nStudent = ', student + ' has grades:')
        for subject in grades:
            # print(subject + ':' + str(grades[subject]))
            list_grades.append(grades[subject])
    return max(list_grades)


student_grades = {
    "Alice": {
        "Math": 95,
        "Science": 87,
        "History": 92
    },
    "Bob": {
        "Math": 88,
        "Science": 91,
        "History": 90
    },
    "Charlie": {
        "Math": 75,
        "Science": 82,
        "History": 78
    }
}

print(get_highest_grade(student_grades))
