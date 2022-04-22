

n = int(input())
l = [input() for i in range(n)]

def is_prime(num):
    for i in range(num):
        if i > 1:
            if num % i == 0:
                return False
    return True

for i in l:
    if is_prime(int(i)):
        print('Prime')
    else:
        print('Not Prime')
