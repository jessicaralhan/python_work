records = [
    (1, "Alice", "Math", 95),
    (2, "Bob", "Math", 85),
    (3, "Charlie", "Science", 90),
    (4, "David", "Science", 88),
    (5, "Eve", "Math", 92),
    (6, "Frank", "Science", 80),
]
# Implement get_unique_subjects(records), which returns a set of unique subjects.
# Implement get_total_marks_by_subjects(records), which returns a dictionary where keys are subject name and values are the total marks.
# Implement get_top_students(records, subject, n), which returns a list of students with the top n highest marks in the given subject.
# Implement filter_students_by_marks(records, subject, min_marks), which returns a list of students who scored above min_marks in the given subject.

# def get_unique_subjects(records):
#     unique_subjects = {}
#     for x in records:
#         unique_subjects.add(x[2])
#     return unique_subjects
# print(get_unique_subjects(records))
    

# def get_unique_subjects(records):
#     return {x[2] for x in records}
# # dict = {
#     "name" : "jess"
# }

# dict.update({"name": "hrishi"})

# def get_total_marks_by_subject(records):
#     total = {}
#     for x in records:
#         subject = x[2]
#         marks = x[3]
#         if subject in total:
#             total[subject] += marks
#         else:
#             total[subject] = marks 
#     return total
# print(get_total_marks_by_subject(records))
# # ('math' : 95)

# def get_top_students(records, subject, n):
#     highest_marks = []
#     for x in records:
#         students = x[1]
    
def filter_students_by_marks(records, subject, min_marks):
    marks = []
    for x in records:
        if x[3] >= min_marks and subject == x[2]:
            marks.append(x)
        
    return marks
# print(filter_students_by_marks(records, "math", 90))

print(5, 5)
print(8)
print(13, end= "")
print(21)