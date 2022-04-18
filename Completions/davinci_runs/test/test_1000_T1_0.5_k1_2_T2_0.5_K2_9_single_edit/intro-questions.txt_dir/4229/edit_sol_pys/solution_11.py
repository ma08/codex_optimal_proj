

from collections import deque

def fizzbuzz(n):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    i = 1
    j = 1
    k = 1
    summ = 0

    for _ in range(n):
        if queue[0] % 15 == 0:
            summ += queue[0]
            queue.append(15*i)
            i += 1
        elif queue[0] % 5 == 0:
            summ += queue[0]
            queue.append(5*j)
            j += 1
        elif queue[0] % 3 == 0:
            summ += queue[0]
            queue.append(3*k)
            k += 1
        else:
            summ += queue[0]
            queue.append(queue[0] + 1)
        queue.popleft()

    return summ

n = int(input())
print(fizzbuzz(n))
