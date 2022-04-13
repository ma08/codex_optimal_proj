

def main():
    N = int(input())
    S = set()
    for _ in range(N):
        s = input()
        S.add(''.join(sorted(s)))
    print(len(S))

if __name__ == '__main__':
    main()
