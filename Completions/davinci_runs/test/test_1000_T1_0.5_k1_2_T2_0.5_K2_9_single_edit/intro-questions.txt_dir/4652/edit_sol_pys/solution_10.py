def main():
    n = int(input())
    s = list(input())
    a = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
    if a > n - a:
        print('Anton')
    elif a < n - a:
        print('Danik')
    else:
        print('Friendship')
main()
