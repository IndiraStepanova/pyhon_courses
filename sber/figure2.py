x=int(input())
for i in range(x+1):
    print(" " * x, sep = "", end = "")
    for j in range(i, 0, -1):
        print(j, sep = "", end = "")
    print()
for i in range(x, 0, -1):
    print(" " * (x-i), sep = "", end = "")
    for j in range(1, i+1):
        print(j, sep = "", end = "")
    print()