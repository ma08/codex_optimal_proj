

a = int(input())

def is_interesting(n):
    if sum(int(i) for i in str(n)) % 4 == 0:
        return True
    return False

while not is_interesting(a):
    a += 1

print(a)