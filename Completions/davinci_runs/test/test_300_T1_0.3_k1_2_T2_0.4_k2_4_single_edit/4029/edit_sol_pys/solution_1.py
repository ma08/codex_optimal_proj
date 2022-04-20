

n = int(input())

if n % 25 == 0:
    print(0)
else:
    n = str(n)
    if n[-1] == '0' or n[-1] == '5' or n[-1] == '2' or n[-1] == '7':
        print(1)
    else:
        print(-1)
