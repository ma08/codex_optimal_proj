

#Solution

a = int(input())

def is_interesting(n):
    return sum(int(i) for i in str(n)) % 4 == 0

while not is_interesting(a):
    a += 1
print(a)