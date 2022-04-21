

def main():
    x = int(input())
    count = 0
    sum = 100
    while sum < x:
        count += 1
        sum += sum // 100
    print(count)

if __name__ == '__main__':
    main()
