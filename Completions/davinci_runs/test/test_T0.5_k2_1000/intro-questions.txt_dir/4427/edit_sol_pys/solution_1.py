
def main():
    r, d, x_2000 = map(int, input().split())
    for i in range(1, 11):
        print(r * x_2000 - d)
        x_2000 = r * x_2000 - d

if __name__ == '__main__':
    main()
