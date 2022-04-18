
def main():
    k = int(input())
    current = 7
    index = 1
    if k % 2 == 1:
        while current % k != 0:
            current = current * 10 + 7
            index += 1
    else:
        while (current % k != 0) and (current % 2 != 0):
            current = current * 10 + 7
            index += 1
    if current % k == 0:
        print(index)
    else:
        print(-1)

if __name__ == '__main__':
    main()
