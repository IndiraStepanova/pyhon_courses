a = [str(current) for current in input()]
same_name = False
my_set = set()
my_set.add(a[0])
print(a[0], end = "")
for current in a[1:]:
    if current in my_set:
        same_name = True
        print(current, end = "")
    else:
        same_name = False
        print('*', end = "")



