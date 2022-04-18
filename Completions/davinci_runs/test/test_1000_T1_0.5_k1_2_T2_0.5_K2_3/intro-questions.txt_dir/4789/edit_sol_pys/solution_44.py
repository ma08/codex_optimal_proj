

def main():
    K = int(input())
    desks = [int(input()) for i in range(K)]
    current_desk = 1
    passes_ = 0
    while any(d > current_desk for d in desks):
        current_desk = max(d for d in desks if d <= current_desk)
        passes_ += 1
    print(passes_)

if __name__ == '__main__':
    main()
