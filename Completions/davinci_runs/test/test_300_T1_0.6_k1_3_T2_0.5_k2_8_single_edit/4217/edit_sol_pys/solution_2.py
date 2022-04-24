

def main():
    # Get input
    N, M = map(int, input().split())

    # Init
    food_list = [[] for _ in range(N)]
    for i in range(N):
        K = int(input().split()[0])
        food_list[i] = list(map(int, input().split()))

    # Main
    answer = 0
    for i in range(1, M+1):
        if all(i in food for food in food_list):
            answer += 1
    print(answer)

if __name__ == '__main__':
    main()
