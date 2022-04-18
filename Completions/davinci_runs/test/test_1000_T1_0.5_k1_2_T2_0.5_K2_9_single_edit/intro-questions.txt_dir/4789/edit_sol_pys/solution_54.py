

def main():
    K = int(input())
    desks = [int(input()) for i in range(K)]
    current_desk = 1
    passes = 0
    while any(b > current_desk for b in desks):
        current_desk = max(b for b in desks if b <= current_desk)
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
