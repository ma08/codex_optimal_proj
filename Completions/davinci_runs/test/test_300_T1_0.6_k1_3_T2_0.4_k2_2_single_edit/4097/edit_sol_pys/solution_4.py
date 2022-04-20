
def solve(n, sequence):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        diff = sequence[1] - sequence[0] # находим разность между первыми двумя элементами массива
        i = 2
        while i < n:
            if sequence[i] - sequence[i-1] != diff: # проверяем разность между соседними элементами массива
                return -1 # если не равна первой разности, то возвращаем -1
            i += 1
        return 0 # иначе возвращаем 0


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(solve(n, sequence))
