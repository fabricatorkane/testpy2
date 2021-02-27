import random
class NegVal(Exception):
    pass
class Necorr(Exception):
    pass

try:
    X = []
    x = int(input('Введите число строк: '))
    if x<=0:
        raise NegVal('Вы ввели отрицательное число')
    y = int(input('Введите число столбцов: '))
    if y<=0:
        raise NegVal('Вы ввели отрицательное число')
    a = int(input('Введите начало для выборки: '))
    b = int(input('Введите конец для выборки: '))
    if a>b:
        raise Necorr('Начало диапазона не может быть больше конца')

    for i in range(x):
            X.append([])
            for j in range(y):
                X[i].append(random.randint(a, b))
    print(X)

except NegVal as N:
    print(N)
except Necorr as Nec:
    print(Nec)
except ValueError:
    print('Нельзя вводить нецелые числа и буквы!')