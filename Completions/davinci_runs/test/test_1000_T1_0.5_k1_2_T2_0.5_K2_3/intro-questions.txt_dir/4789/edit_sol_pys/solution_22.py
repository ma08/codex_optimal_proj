

def main():
    K = int(input())
    desks = [int(input()) for i in range(K)]
    current_desk = 1
    passes_count = 0
    while any(desk > current_desk for desk in desks)
        current_desk = max(desk for desk in desks if desk <= current_desk)
        passes_count += 1
    print(passes_count)

if __name__ == '__main__':
    main()
