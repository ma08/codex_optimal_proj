

def main():
    a, b = map(int, input().split())
    if a == b:
        print(2 * a)
    else:
        print((a + b) * 2)

main()
