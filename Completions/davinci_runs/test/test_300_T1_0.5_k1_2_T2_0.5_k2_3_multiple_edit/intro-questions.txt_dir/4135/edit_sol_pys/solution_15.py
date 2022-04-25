
def main():
    n = int(input())
    t = input()
    d = n//2
    print(t[d:], end="")
    print(t[:d][::-1], end="")

main()
