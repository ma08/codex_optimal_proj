

n = int(input())
s = input()

if s[0] == ')':
    print(0)
else:
    count = 1
    for i in range(1, n):
        if s[i] == ')':
            count -= 1
        else:
            count += 1
        if count < 0:
            print(0)
            exit()
    print(count)