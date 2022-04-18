
def main():
    N, B, H, W = map(int, input().split())
    min_cost = B

    for _ in range(H):
        cost_per_person = int(input().strip())
        available_beds = list(map(int, input().strip().split()))

        for beds in available_beds:
            if beds >= N:
                min_cost = min(min_cost, cost_per_person * N)

    if min_cost == B:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
