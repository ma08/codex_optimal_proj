

def main():
    x = float(input())

    i = 1
    while i < 10:
        j = 1
        while j < 10:
            if i / j == x and i % j == 0:
                print(i, "/", j)
            j = j + 1
        i = i + 1

if __name__ == '__main__':
    main()
