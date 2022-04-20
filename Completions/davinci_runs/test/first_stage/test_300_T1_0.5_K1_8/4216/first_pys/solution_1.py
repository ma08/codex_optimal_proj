

def main():
    N = int(input())
    ans = 1e10
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans = min(ans, len(str(i)) + len(str(N//i)))
    print(ans)

if __name__ == '__main__':
    main()