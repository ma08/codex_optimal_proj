

def main():
    r, D, x2000 = map(int, input().split())
    for i in range(1, 11):
        print(r * x2000 - D, end="\n")
        x2000 = r * x2000 - D, end="\n"

if __name__ == '__main__':
    main()
