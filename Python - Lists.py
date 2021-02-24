list = []
n = int(input())
for i in range(n):
    p = input().split()
    if p[0] == "insert":
        list.insert(int(p[1]), int(p[2]))
    elif p[0] == "print":
        print(list)
    elif (p[0] == "remove"):
        list.remove(int(p[1]))
    elif p[0] == "append":
        list.append(int(p[1]))
    elif p[0] == "sort":
        list.sort()
    elif p[0] == "pop":
        list.pop()
    elif p[0] == "reverse":
        list.reverse()
