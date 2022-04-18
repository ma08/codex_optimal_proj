

def is_substring(s1, s2):
    return len(s1) <= len(s2) and s1 in s2

def main():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    strings.sort(key=len)
    for i in range(len(strings)):
        if i == 0:
            continue
        if not is_substring(strings[i], strings[i-1]):
            print('NO')
            return
    print('YES')
    print('\n'.join(strings))

if __name__ == '__main__':
    main()
