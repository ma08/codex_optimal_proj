

a = int(input())

while True:
    if sum(map(int,list(str(a))))%4 == 0:
        print(a)
        break
    else:
        a += 1