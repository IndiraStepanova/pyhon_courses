'''Лена узнала, что на ее любимом маркетплейсе действует интересная акция. Согласно её условиям, организаторы 
раздают подарки всем клиентам, впервые сделавшим заказ, номер которого окажется палиндромом. Лена заметила, 
что номера заказов формируются в порядке возрастания, и решила перехитрить организаторов: в нужный момент 
очень быстро оформить подряд несколько мелких заказов, чтобы гарантированно «выбить» счастливый номер.

Помогите Лене определить, насколько близко номер текущего заказа к ближайшему за ним «счастливому» номеру.

Примечание: Число является палиндромом, если читается слева направо так же, как справа налево.
Пример палиндрома: 123321

Примечание к примерам:

2 = 656 - 654
7 = 5555 - 5548'''

def polyndrom(current):
    lelf_part = 0
    right_part = len(current)-1
    while lelf_part <= right_part:
        if current[lelf_part] == current[right_part]:
            lelf_part += 1
            right_part -= 1
        else:
            return False
    return True

current_order = input()
ini_current_order = int(current_order)
result = 0
while polyndrom(current_order) == False:
    int_CO = int(current_order)
    int_CO += 1
    current_order = str(int_CO)
last = int(current_order)
result = last - ini_current_order
print(result)



