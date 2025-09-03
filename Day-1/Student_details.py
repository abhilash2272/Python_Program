n=int(input("Enter number of students"))
for i in range(n):
    snumber=int(input("Enter the student number"))
    sname=input("Enter the name")
    m1=int(input("Enter the student marks"))
    m2=int(input("Enter the student marks"))
    m3=int(input("Enter the student marks"))
    total=m1+m2+m3
    avg=total/3
    round(avg,2)
    print("The average is ",avg,"Total is ",total)