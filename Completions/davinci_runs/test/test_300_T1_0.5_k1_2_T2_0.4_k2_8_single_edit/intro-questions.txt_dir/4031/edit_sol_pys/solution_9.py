
def check_strings(strings):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i] not in strings[j]:
                return False
    return True


n = int(input())
strings = [input() for i in range(n)]
strings.sort(key=lambda x: len(x))

if check_strings(strings):
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')
