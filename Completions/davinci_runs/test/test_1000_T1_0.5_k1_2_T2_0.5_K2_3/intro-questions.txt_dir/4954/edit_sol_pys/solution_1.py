

def main():
    N, B, H, W = map(int, input().split()) # N = number of people, B = budget, H = number of hotels, W = number of weeks
    min_cost = B # minimum cost

    for _ in range(H):
        cost_per_person = int(input())
        available_weeks = list(map(int, input().split()))

        for week in available_weeks:
            if week >= N:
                min_cost = min(min_cost, cost_per_person * N)

    if min_cost == B:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
