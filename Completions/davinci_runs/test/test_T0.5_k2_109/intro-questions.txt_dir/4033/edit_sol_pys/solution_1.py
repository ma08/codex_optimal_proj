

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == b:
        print(4 * a)
    else:
        print((a + b) * 2)

main()
