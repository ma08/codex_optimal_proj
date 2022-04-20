

def main():
    n = int(input())
    s = [input() for _ in range(n)]

    s.sort()

    for i in range(n):
        print(s[i])

main()
