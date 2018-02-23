# Условие
# Даны три целых числа. Выведите значение наименьшего из них.
a = int(input("Первое число "))
b = int(input("Второе число "))
c = int(input("Третье число "))
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
