
def main():
    n = int(input())
    t = input()
    for i in range(n,0,-1):
        if n%i == 0:
            d = i
            break
    print(t[d:]+t[:d][::-1], end="")

main()
