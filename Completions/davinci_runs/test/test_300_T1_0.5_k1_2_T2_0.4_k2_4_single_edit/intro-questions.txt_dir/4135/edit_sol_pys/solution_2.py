

def main():
    n = int(input())
    t = input()
    print(t[n:], end="")
    print(t[:n][::-1], end="")

main()
