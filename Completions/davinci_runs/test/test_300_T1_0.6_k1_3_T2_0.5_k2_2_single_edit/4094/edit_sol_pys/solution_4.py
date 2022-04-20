

def main():
    k = int(input())
    current = 7 % k
    index = 1
    while current != 0:
        current = (current * 10 + 7) % k
        index += 1
    if current % k == 0:
        print(index)
    else:
        print(-1)

if __name__ == '__main__':
    main()
