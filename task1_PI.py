# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from cmath import pi

def stepen (d):
    value = 1
    while d < 0.1:
        d = round(d/0.1,value+5)
        value = value+1
    return (value)



print('Введите точность, с которой необходимо выести число Pi в виде 0.1 или 0.01 или так далее, разделяя целую и дробные части ТОЧКОЙ')
d = float(input())
a = stepen(d)
print(f'Число Pi c точностью {d} равно {round(pi,a)}')
