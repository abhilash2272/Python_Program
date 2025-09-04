cons_num = int(input("Enter the number: "))
cons_name = input("Enter the name: ")
pmr = int(input("Enter the present month reading: "))
lmr = int(input("Enter the last month reading: "))
tu = pmr - lmr
print("The consumer number is", cons_num)
print("The consumer name is", cons_name)
if tu>300:
    curr_bill=50*3.80+50*4.20+100*5.10+100*6.30+(tu-300)*7.50
    print(curr_bill)
elif tu>200 and tu<=300:
    curr_bill=50*3.80+50*4.20+100*5.10+(tu-200)*6.30
    print(curr_bill)
elif tu>100 and tu<=200:
    curr_bill=50*3.80+50*4.20+(tu-100)*5.10
    print(curr_bill)
elif tu>100 and tu<=51:
    curr_bill=50*3.80+(tu-100)*4.20
    print(curr_bill)
else:
    curr_bill=tu*3.80
    print(curr_bill)
    
