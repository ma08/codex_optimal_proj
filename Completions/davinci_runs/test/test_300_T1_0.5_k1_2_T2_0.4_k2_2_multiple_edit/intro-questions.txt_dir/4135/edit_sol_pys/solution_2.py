

def main():
    n = int(input())
    t = input()
    print(t[n:] + t[:n][::-1])

main()
