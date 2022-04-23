

from collections import deque

def fizzbuzz(n):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) # создаем очередь
    i = 1
    j = 1
    k = 1
    summ = 0

    for _ in range(n):
        if queue[0] % 15 == 0: # если первый элемент очереди делится на 15 без остатка
            summ += queue[0]
            queue.append(15*i)
            i += 1
        elif queue[0] % 5 == 0: # если первый элемент очереди делится на 5 без остатка
            summ += queue[0]
            queue.append(5*j)
            j += 1
        elif queue[0] % 3 == 0: # если первый элемент очереди делится на 3 без остатка
            sum += queue[0]
            queue.append(3*k)
            k += 1
        else: # если первый элемент очереди не делится на 3, 5 и 15 без остатка
            sum += queue[0]
            queue.append(queue[0] + 1)
        queue.popleft()

    return sum

n = int(input())
print(fizzbuzz(n))
