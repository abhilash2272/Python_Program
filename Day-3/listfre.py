def fre():
    l = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        l.append(int(input("Enter element: ")))
    print("Frequency of all elements:")
    for i in range(n):
        count = 0
        for j in range(n):
            if l[i] == l[j]:
                count += 1
        if l[i] not in l[:i]:
            print(f"{l[i]} : {count}")
fre()