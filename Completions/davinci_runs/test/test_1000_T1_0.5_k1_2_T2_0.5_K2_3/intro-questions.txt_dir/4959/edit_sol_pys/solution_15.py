
def main():
    empty, full, cap = map(int, input().split())
    count = 0
    while empty + full >= cap:
        count += (empty + full) // cap
        empty, full = (empty + full) % cap, empty // cap
    print(count)

if __name__ == '__main__':
    main()
