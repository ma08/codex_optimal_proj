

def main():
    N, M, H, W = map(int, input().split())
    min_cost = M

    for _ in range(H):
        cost_per_person = int(input())
        available_beds = list(map(int, input().split()))

        for beds in available_beds:
            if beds >= N:
                min_cost = min(min_cost, cost_per_person * N)

    if min_cost == M:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
