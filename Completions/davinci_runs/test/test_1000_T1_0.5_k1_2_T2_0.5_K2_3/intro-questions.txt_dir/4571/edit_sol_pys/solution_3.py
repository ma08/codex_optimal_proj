

def main():
    N -= 1
    N, M = map(int, input().split())
    success_prob = 1
    for i in range(N):
        success_prob /= 2
    print(int(1900*M*success_prob + 100*(N)))

if __name__ == '__main__':
    main()
