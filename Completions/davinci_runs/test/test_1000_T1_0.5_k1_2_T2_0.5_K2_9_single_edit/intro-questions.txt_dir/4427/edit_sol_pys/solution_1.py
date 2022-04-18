

def main():
    r, D, x = map(int, input().split())
    for i in range(1, 11):
        print(r * x - D)
        x = r * x - D

if __name__ == '__main__':
    main()
