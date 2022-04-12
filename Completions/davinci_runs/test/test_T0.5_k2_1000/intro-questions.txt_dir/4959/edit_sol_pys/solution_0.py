

def main():
    empty, full, capacity = map(int, input().split())
    n = (empty + full) // capacity
    left = (empty + full) % capacity
    while n + left >= capacity:
        n += left // capacity
        left = (left % capacity) + (left // capacity)
    print(n)

if __name__ == '__main__':
    main()
