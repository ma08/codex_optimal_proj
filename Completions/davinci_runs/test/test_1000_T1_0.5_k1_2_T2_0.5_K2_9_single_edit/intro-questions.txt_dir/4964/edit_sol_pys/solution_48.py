

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        print(a, b)

main()
