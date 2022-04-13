

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(1, 11):
        x = r * x2000 - D
        print(x)
        x2000 = x

if __name__ == '__main__':
    main()
