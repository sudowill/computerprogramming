students = input("How many students are there? ")
students = int(students)
classes = input("How many classes are there? ")
classes = int(classes)
groups = int(students / classes)
groupsremainder = int(students % classes)

print("There are", groups, "groups of students and a group of ", groupsremainder,"remainding")
