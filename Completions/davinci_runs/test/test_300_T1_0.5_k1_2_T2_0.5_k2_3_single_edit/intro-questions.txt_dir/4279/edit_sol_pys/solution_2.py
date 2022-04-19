
import math

def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    data = input().split()
    data = [int(i) for i in data]
    data.sort()
    print(data)
    print(min(data))
    print(max(data))
    print(sum(data) / len(data))
    print(data[len(data) // 2])

if __name__ == '__main__':
    main()
