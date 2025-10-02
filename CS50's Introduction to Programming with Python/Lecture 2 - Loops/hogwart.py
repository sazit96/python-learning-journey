# # Create a list of students
# students = ["sazit", "ehosanul", "islam"]

# # Print the 3rd student (index 2, since Python starts from 0)
# print(students[2])

# # Loop directly through the list (prints each student name)
# for student in students:
#     print(student)

# # Loop using index (useful if you also want the position/number)
# for i in range(len(students)):
#     print(i + 1, students[i])  # i+1 for human-friendly numbering


student = {
    "sazit":"gazipur",
    "ehosanul": "porabari",
    "islam": "vowride"
}

for s in student: 
    print(s, student[s], sep= " - ")