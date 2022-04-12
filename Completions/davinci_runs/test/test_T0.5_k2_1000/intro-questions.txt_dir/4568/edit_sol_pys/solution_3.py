
N = int(input())
S = input()

def main():
    ans = 0
    for i in range(1, N):
        ans = max(ans, len(set(S[:i]) & set(S[i:])))
    print(ans)

if __name__ == '__main__':
    main()
