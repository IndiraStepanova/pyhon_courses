def basa(): #v
    for i in range(1, 101):
        for j in range(1, 51):
            result = pow(2, i*j)
    return result

def first():
    for i in range(1,101):
        result_1 = 50 * pow(2, i)
    return result_1


def second():
    for i in range(1, 101):
        for j in range(1, 51):
            result= pow(2, (101 - j)*i)
    return result


def third():
    for i in range(1, 101):
        for j in range(1, 51):
            result= pow(2, ((101 - j)*(51 - i)))
    return result



def forth():
    for i in range(1, 51):
        for j in range(1, 101):
            result= pow(2, i * j)
    return result

def fifth():
    for i in range(1, 101):
        for j in range(1, 51):
            result= pow(2, (51-i)*j)
    return result

def sixth():
    for i in range(1, 101):
        result= pow(2, 50*i)
    return result


for i in range(1,201):
    if i%1==0 and i%2==0 and i%3==0 and i%4==0 and i%5==0:
        print(i)



