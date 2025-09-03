cons_num = int(input("Enter the number: "))
cons_name = input("Enter the name: ")
pmr = int(input("Enter the present month reading: "))
lmr = int(input("Enter the last month reading: "))
tu = pmr - lmr
curr_bill = tu * 3.8
print("The consumer number is", cons_num)
print("The consumer name is", cons_name)
print("The current bill is", curr_bill)