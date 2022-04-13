from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a.sort(reverse=True)
    for i in a:
        print(i, end=" ")
    print("")

def main():
    while True:
        try:
            solve()
        except:
            break

main()
