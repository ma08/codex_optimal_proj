
def is_substring(s1, s2):
    if len(s1) > len(s2):
        return False
    for i in range(len(s2)):
        if s2[i:i + len(s1)] == s1:
            return True

    return False

def main():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    strings.sort(key=lambda s: len(s))
    for i in range(len(strings)):
        if i == 0:
            continue
        if not is_substring(strings[i], strings[i - 1]):
            print('NO')
            return
    print('YES')
    print('\n'.join(strings))


if __name__ == '__main__':
    main()
