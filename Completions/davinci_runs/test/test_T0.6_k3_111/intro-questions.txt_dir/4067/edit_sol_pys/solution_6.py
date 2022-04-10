
def main():
    n = int(input())
    s = input()
    assert len(s) == n, "len(s) != n"
    assert n % 3 == 0, "n % 3 != 0"
    assert all([c in '012' for c in s]), "s contains characters other than 0, 1, 2"
    s = list(s)
    for i in range(n):
        if s[i] == '2':
            s[i] = '0'
            break
    for i in range(n):
        if s[i] == '1':
            s[i] = '0'
            break
    for i in range(n):
        if s[i] == '2':
            s[i] = '1'
            break
    print(''.join(s))


if __name__ == "__main__":
    main()
