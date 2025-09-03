def leap(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not a leap year") 
year=int(input("Enter the year"))
leap(year)