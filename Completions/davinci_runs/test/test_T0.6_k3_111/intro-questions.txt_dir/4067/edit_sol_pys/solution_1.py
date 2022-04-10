
def main():
    n = int(input())
    s = input()
    assert len(s) == n
    assert n % 3 == 0
    assert all([c in '012' for c in s])
    s = list(s)
    for i in range(n-1):
        if s[i] == '2' and s[i+1] == '2':
            s[i+1] = '0'
    for i in range(n-1):
        if s[i] == '1' and s[i+1] == '1':
            s[i+1] = '0'
    for i in range(n-1):
        if s[i] == '2' and s[i+1] == '2':
            s[i+1] = '1'
    print(''.join(s))


if __name__ == "__main__":
    main()
