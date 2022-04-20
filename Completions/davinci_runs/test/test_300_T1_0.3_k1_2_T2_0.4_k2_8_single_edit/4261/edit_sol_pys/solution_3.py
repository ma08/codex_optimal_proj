

def main():
    a, b, c = map(int, input().split())
    bottle2 = c - (a - b)
    print(max(0, bottle2))

main()
