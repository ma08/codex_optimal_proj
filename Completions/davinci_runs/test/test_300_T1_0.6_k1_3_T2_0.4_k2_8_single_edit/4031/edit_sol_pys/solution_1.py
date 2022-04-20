

def is_substring(s1, s2, i):
    return s2.startswith(s1, i)

def main():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    for i in range(len(strings)):
        for j in range(i):
            if is_substring(strings[i], strings[j], 0):
                strings[i], strings[j] = strings[j], strings[i]
    print('YES')
    print('\n'.join(strings))

if __name__ == '__main__':
    main()
