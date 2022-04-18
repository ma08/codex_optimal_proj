
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if sum(a) % 2 == 1 else "NO")



if __name__ == '__main__':
    main()
