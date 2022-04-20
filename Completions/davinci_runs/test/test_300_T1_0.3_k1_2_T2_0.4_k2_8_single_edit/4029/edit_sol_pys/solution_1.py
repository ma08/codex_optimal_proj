

n = int(input())

if n % 25 == 0:
    print(0)
else:
    n = str(n)
    if n[-1] == '0' or n[-1] == '5' or n[-1] == '1' or n[-1] == '6' or n[-1] == '2' or n[-1] == '7' or n[-1] == '3' or n[-1] == '8' or n[-1] == '4' or n[-1] == '9':
        print(1)
    else:
        print(-1)
