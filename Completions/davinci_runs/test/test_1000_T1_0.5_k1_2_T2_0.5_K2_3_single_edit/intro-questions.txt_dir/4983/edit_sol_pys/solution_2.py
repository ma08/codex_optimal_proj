

n = int(input())

while n > 9:
    n = str(n)
    n = [int(i) for i in n]
    n = [i for i in n if i != 0]
    n = [str(i) for i in n]
    n = ''.join(n)
    n = int(n)

print(n)
