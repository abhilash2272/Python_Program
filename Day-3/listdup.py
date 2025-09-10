def dup():
    l = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        l.append(int(input("Enter element: ")))
    dup_count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if l[i] == l[j]:
                count += 1
        if count > 1 and l[i] not in l[:i]:
            dup_count += 1
    print("Total number of duplicate elements:", dup_count)
dup()