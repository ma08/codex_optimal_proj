

def s(n, t):
    for i in range(n, 0, -1):
        if n % i == 0:
            return i, t[:i][::-1]

def main():
    n = int(input())
    t = input()
    d = s(n, t)
    print(t[d:], end="")
    print(t[:d][::-1], end="")

main()
