

def main():
    n = int(input())
    values = list(map(int, input().split()))
    values.sort()
    while len(values) > 1:
        values.append((values[0] + values[1]) / 2)
        values.pop(0)
        values.pop(0)
        values.sort()
    print(values[0])

if __name__ == '__main__':
    main()