

def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print('No')
        return
    else:
        for i in range(N//2):
            if S[i] != S[i + N//2]:
                print('No')
                return
        print('Yes')
        return

if __name__ == '__main__':
    main()
