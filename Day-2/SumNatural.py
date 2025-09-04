def SumN(num):
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print(sum)
num=int(input("Enter the number"))
SumN(num)