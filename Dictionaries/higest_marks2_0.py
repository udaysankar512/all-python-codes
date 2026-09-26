student_marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88,
    "Arjun": 95,
    "Neha": 89
}
highest_marks = max(student_marks,key=student_marks.get)
details = [highest_marks,student_marks[highest_marks]]
print("The top is :",details)