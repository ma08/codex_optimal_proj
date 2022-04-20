

def main():
    k = int(input())
    current = 7
    index = 0
    if k % 2 == 1:
        while (current % k != 0) and (current % 2 != 0):
            current = current * 10 + 7
        if current % k == 0:
            print(index)
        else:
            print(-1)
            index += 1
    else:
        print(-1)

if __name__ == '__main__':
    main()
