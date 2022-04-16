

def main():
    K = int(input())
    desks = [int(input()) for i in range(K)]
    current_desk = 1
    passes = 0
    while any(desk > current_desk for desk in desks):  # while there are desks that are higher than the current desk
        current_desk = max(desk for desk in desks if desk <= current_desk)  # find the highest desk that is lower than the current desk
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
