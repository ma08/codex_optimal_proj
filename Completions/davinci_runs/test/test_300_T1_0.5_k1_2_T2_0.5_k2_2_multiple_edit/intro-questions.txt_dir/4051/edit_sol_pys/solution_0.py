

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    for i in range(n):
        print(a[i] * "#")
    print("YES" if sorted(a) == a else "NO")

main()
