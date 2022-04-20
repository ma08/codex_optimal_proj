def main():
    N, K = map(int, input().split())
    S = input()
    if S[K - 1] == 'A':
        print('a')
    elif S[K - 1] == 'B':
        print('b')
    else:
        print('c')



if __name__ == '__main__':
    main()
