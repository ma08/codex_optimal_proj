

def main():
    year = int(input())
    while True:
        if year % 4 == 0:
            print(year)
            break
        else:
            year += 1

if __name__ == '__main__':
    main()
