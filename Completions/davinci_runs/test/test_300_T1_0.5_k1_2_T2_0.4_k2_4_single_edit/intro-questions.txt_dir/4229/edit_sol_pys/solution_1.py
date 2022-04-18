

from collections import deque

def fizzbuzz(n):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) #initialize queue
    i = 1 #initialize counter for multiples of 15
    j = 1 #initialize counter for multiples of 5
    k = 1 #initialize counter for multiples of 3
    sum = 0 #initialize sum

    for _ in range(n): #iterate n times
        if queue[0] % 15 == 0: #check if the first element in the queue is a multiple of 15
            sum += queue[0] #add the first element in the queue to the sum
            queue.append(15*i) #append the next multiple of 15 to the queue
            i += 1 #increment the counter for multiples of 15
        elif queue[0] % 5 == 0: #check if the first element in the queue is a multiple of 5
            sum += queue[0] #add the first element in the queue to the sum
            queue.append(5*j) #append the next multiple of 5 to the queue
            j += 1 #increment the counter for multiples of 5
        elif queue[0] % 3 == 0: #check if the first element in the queue is a multiple of 3
            sum += queue[0] #add the first element in the queue to the sum
            queue.append(3*k) #append the next multiple of 3 to the queue
            k += 1 #increment the counter for multiples of 3
        else:
            sum += queue[0] #add the first element in the queue to the sum
            queue.append(queue[0] + 1) #append the next number to the queue
        queue.popleft() #pop the first element in the queue

    return sum #return the sum

n = int(input()) #get the number of iterations
print(fizzbuzz(n)) #print the sum
