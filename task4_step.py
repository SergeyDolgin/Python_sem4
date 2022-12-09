# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9


from random import randint
import itertools

def koef(k):
    koef = [randint(0,100) for i in range (k)]
    return koef

def urov(k, numbers):
    f = ['*x^']*(k-1) + ['*x']
    mnogochlen = [[a, b, c] for a, b, c in itertools.zip_longest(numbers, f, range(k, 1, -1), fillvalue= '') if a != 0]
    for x in mnogochlen:
        x.append(' + ')
    mnogochlen = list(itertools.chain(*mnogochlen))
    mnogochlen[-1] = ' = 0'
    return "".join(map(str, mnogochlen)).replace(' 1*x',' x')

k = int(input('Введите степень первого многочлена '))
numbers = koef(k)
end_list1 = urov(k, numbers)
print(f'Многочлен степени {k} со случайными коэффициентами ', end_list1)

with open('text1.txt', 'w') as data:
    data.write(end_list1)

k = int(input('Введите степень второго многочлена '))
numbers = koef(k)
end_list2 = urov(k, numbers)
print(f'Многочлен степени {k} со случайными коэффициентами ', end_list2)

with open('text2.txt', 'w') as data:
    data.write(end_list2)




