import itertools

def first_work():
    hour = int(input('Сколько часов крестьянин пахал поле: '))
    coin = int(input('Сколько помещик дает монет за час труда: '))
    happines = int(input('Сколько помещик отдаст с барского плеча в день весеннего равновесия: '))
    profit = (hour * coin) + happines
    return profit


def sixth_work(start_number):
    for i in itertools.count(start_number):
        print(i)
        if i > 9:
            break

def sixth_work_2():
    c = 0
    a = int(input('Сколько копий списка нужно? '))
    b = input('Введите содержание списка ')
    for i in itertools.cycle(b):
        if c == a:
            break
        print(i)
        c += (1/len(b))
