
import sys

def get_input():
    n = int(input())
    q = [int(x) for x in input().split()] # преобразование строки в список
    return n, q

def check_permutation(n, q):
    if len(q) != n - 1: # сравниваем количество элементов в массиве q с количеством элементов последовательности
        return False
    if n == 1: # если длина последовательности равна 1, то выводим True
        return True
    for i in q:
        if abs(i) >= n: # если элемент массива q больше или равен длине последовательности, то выводим False
            return False
    return True

def create_permutation(n, q):
    if n == 1:
        return [1]
    p = [0] * n
    p[0] = q[0] # заполняем первый элемент массива p
    p[1] = q[0] + q[1]
    for i in range(2, n):
        p[i] = p[i-1] + q[i-1] # заполняем остальные элементы массива по условию
    return p

def print_permutation(p):
    print(" ".join([str(x) for x in p])) # выводим последовательность

def main():
    n, q = get_input() # получаем последовательность
    if not check_permutation(n, q): # проверяем последовательность на возможность создания перестановки
        print(-1)
        return
    p = create_permutation(n, q) # создаем перестановку
    print_permutation(p)

if __name__ == "__main__":
    main()
