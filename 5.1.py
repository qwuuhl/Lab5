'''
Задача №1
Напишіть функцію, яка створює комбінацію із двох послідовностей цілих чисел,
впорядковану за зростанням.

Вхідні дані:
1 4 0 12 4 5
24 1 2 10 8
Вихідні дані:
0 1 1 2 4 4 5 8 10 12 24

Автор: Задворна Анастасія Богданівна
'''

def solution():
    list1 = list(map(int, input("Введіть послідовність 1: ").split()))
    list2 = list(map(int, input("Введіть послідовність 2: ").split()))

    combined_list = list1 + list2
    
    sorted_list = sorted(combined_list)
    sorted_list = list(map(str, sorted_list))

    return ' '.join(sorted_list)
    
    
result = solution()
print(result)
