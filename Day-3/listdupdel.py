def deldup():
    l = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        l.append(int(input("Enter element: ")))
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if l[i] == l[j]:
                del l[j]
            else:
                j += 1
        i += 1
    print("List after removing duplicates:", l)

deldup()