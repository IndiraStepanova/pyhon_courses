objects = [1,2,3,4,5,6,7,88,99,88,9]
''''
ans = 0
previous = objects[0]
objects.sort()
same_name = False
for current in objects[1:]: # доступная переменная objects
    if current == previous:
        same_name = True

    else:
        previous = current
        same_name = False
    ans += 1

print(ans)'''

'''
my_set = set()
for obj in objects: # доступная переменная objects
    my_set.add(id(obj))
print(len(my_set))
'''
list_lenght = len(objects)
ans = list_lenght

for i in range(list_lenght):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
print(ans)


