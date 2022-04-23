# В первой строке вводится количество чисел N. Во второй строке вводятся N чисел. Выведите все числа, которые встречаются в последовательности, более одного раза.
n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicates(a):
    a = set(a)
    return a

b = remove_duplicates(a)
print(b)
