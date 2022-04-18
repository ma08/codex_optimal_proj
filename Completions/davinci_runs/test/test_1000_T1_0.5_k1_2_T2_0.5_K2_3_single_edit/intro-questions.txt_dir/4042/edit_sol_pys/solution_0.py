

def main():
    x = float(input())

    for i in range(1, 10):
        if x * i % 1 == 0:
            print(int(x * i), i)
            break

if __name__ == '__main__':
    main()
