

from collections import deque

def fizzbuzz(n):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # queue of numbers
    i = 1
    j = 1
    k = 1
    sum = 0  # sum of fizzbuzz numbers

    for _ in range(n):
        if queue[0] % 15 == 0: # if number is divisible by 15
            sum += queue[0] # add number to sum
            queue.append(15*i) # add next number to queue
            i += 1
        elif queue[0] % 5 == 0: # if number is divisible by 5
            sum += queue[0] # add number to sum
            queue.append(5*j) # add next number to queue
            j += 1
        elif queue[0] % 3 == 0: # if number is divisible by 3
            sum += queue[0] # add number to sum
            queue.append(3*k) # add next number to queue
            k += 1
        else:
            sum += queue[0] # add number to sum
            queue.append(queue[0] + 1) # add next number to queue
        queue.popleft() # remove number from queue

    return sum # return sum of fizzbuzz numbers

n = int(input())
print(fizzbuzz(n))
