
from collections import deque

def fizzbuzz(n):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    i = 1
    j = 1
    k = 1
    sum = 0

    for _ in range(n):
        if queue[0] % 15 == 0:
            sum += queue[0]
            queue.append(15*i)
            i += 1
        elif queue[0] % 5 == 0:
            sum += queue[0]
            queue.append(5*j)
            j += 1
        elif queue[0] % 3 == 0:
            sum += queue[0]
            queue.append(3*k)
            k += 1
        else:
            sum += queue[0]
            queue.append(queue[0] + 1)
        queue.popleft()

    return sum

n = int(input())
print(fizzbuzz(n))
