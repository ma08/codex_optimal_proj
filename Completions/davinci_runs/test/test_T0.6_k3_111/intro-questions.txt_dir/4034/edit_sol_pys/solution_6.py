

n = int(input())
s = input()

if len(set(s)) == 1:
    print('YES')
    print('0' * n)
elif len(set(s)) == n:
    print('YES')
    print('1' * n)
else:
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    char_count = list(char_count.items())
    char_count.sort(key=lambda x: x[0])

    if len(char_count) == 2:
        if char_count[0][1] == 1 or char_count[1][1] == 1:
            print('YES')
            if char_count[0][1] == 1:
                print('0' * char_count[0][1] + '1' * char_count[1][1])
            else:
                print('1' * char_count[0][1] + '0' * char_count[1][1])
        else:
            print('NO')
    elif len(char_count) == 3:
        if char_count[0][1] == 1 and char_count[2][1] == 1:
            print('YES')
            if char_count[0][0] < char_count[1][0]:
                print('0' * char_count[0][1] + '1' * char_count[1][1] + '0' * char_count[2][1])
            else:
                print('0' * char_count[2][1] + '1' * char_count[1][1] + '0' * char_count[0][1])
        else:
            print('NO')
    else:
        print('NO')
