"""Василий постоянно забывает не только ПИН-коды от банковских карт, но и пароли от различных онлайн-сервисов. Чтобы победить 
свою забывчивость, он решил выработать для себя такое правило придумывания паролей: каждый пароль должен состоять из четного 
количества символов, и при этом первая половина пароля должна быть «анаграммно меньше» второй его половины. Теперь Василию 
нужен алгоритм, проверяющий, удовлетворяет ли придуманный пароль заданному условию.
Вам дано n пар строк одинаковой длины (каждая строка – половина пароля).

Строка s считается анаграммно меньше строки t, если существуют строка s' и строка t' такие что:
s' получается из s перестановкой букв
t' получается из t перестановкой букв
s' лексикографически меньше, чем t'

Для каждой пары строк si, ti определите правда ли, что si анаграммно меньше чем ti."""

def rule(first_part, sec_part):
    first_simbol = 0
    sec_simbol = 0
    while first_simbol <= sec_simbol:
        if first_part[first_simbol] > sec_part[sec_simbol]:
            first_simbol += 1
            sec_simbol += 1
        else:
            return False
        return True

def good_password(lenght, f_part, s_part):
    cnt =0
    while cnt <= lenght:
        if rule(f_part, s_part):
            cnt += 1
        else:
            return False
        return True

pairs = int(input())
cnt = 0
while cnt <= pairs:
    pairs = int(input())
    if good_password(2, "bc", "ca") == True:
        print ("Yes")
    else:
        print("No")
    cnt += 1


    


 
 


