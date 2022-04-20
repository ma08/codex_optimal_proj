

n = input()

if int(n) % 25 == 0:
    print(0)
else:
    n = str(n)
    if n[-1] == '0' or n[-1] == '5':
        print(1)
    else:
        print(-1)
