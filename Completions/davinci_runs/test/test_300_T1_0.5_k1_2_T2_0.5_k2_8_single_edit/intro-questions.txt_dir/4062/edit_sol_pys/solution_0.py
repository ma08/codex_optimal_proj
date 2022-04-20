

def main():
    a, b, c, d = map(int, input().split()) # a, b, c, d = (int(input()) for _ in range(4))
    print(max(a * c, a * d, b * c, b * d)) # print(max(a * c, a * d, b * c, b * d, key=int))

if __name__ == '__main__':
    main()
