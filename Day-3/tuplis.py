def stu(t):
    highest_marks = t[0][1]
    highest_name = t[0][0]
    for student in t:
        if student[1] > highest_marks:
            highest_marks = student[1]
            highest_name = student[0]
    print(f"Highest marks: {highest_name} ({highest_marks})")
    print("Students who scored more than 75 marks:")
    for student in t:
        if student[1] > 75:
            print(student[0])
l = []
for i in range(5):
    roll = int(input("Enter roll: "))
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    l.append((name, marks))
stu(tuple(l))