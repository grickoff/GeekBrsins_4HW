from _functools import reduce

def red_def(a, b):
    return a * b

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).

custom_list = [i for i in range(100, 1001) if i % 2 < 1]
print(custom_list)

# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

print(reduce(red_def, custom_list))
