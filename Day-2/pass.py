n = int(input("Enter number of students"))
for i in range(n):
    snumber = int(input("Enter the student number"))
    sname = input("Enter the name")
    m1 = int(input("Enter the student marks"))
    m2 = int(input("Enter the student marks"))
    m3 = int(input("Enter the student marks"))
    total = m1 + m2 + m3
    avg = round(total / 3, 2)
    print("The average is", avg, "Total is", total)
    def check_pass(avg):
        if avg > 80:
            print("Distinction")
        elif avg >= 60:
            print("First Class")
        elif avg >= 50:
            print("Second Class")
        elif avg >= 40:
            print("Pass")
        else:
            print("Fail")
    check_pass(avg)