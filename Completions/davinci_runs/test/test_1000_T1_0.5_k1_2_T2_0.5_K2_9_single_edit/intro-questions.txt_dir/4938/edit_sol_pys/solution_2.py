

N = int(input())
queue = list(input())

def is_valid(queue):
    for i in range(len(queue)):
        if queue[i] == 'W':
            if i + 1 < len(queue) and queue[i+1] == 'M':
                return False
        else:
            if i + 1 < len(queue) and queue[i+1] == 'W':
                return False
    return True

def swap(queue, i, j):
    queue[i], queue[j] = queue[j], queue[i]

def solve(queue):
    count = 0
    while not is_valid(queue):
        for i in range(len(queue)):
            if i + 1 < len(queue) and queue[i] == 'W' and queue[i+1] == 'M':
                swap(queue, i, i+1)
                count += 1
    return count

print(solve(queue))
