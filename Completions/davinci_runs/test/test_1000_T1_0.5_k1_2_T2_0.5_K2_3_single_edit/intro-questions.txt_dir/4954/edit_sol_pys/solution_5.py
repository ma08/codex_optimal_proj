

def main():
    N, B, H, W = map(int, input().split())  # N - number of people
    min_cost = B  # min_cost - minimum cost of travel

    for _ in range(H):
        cost_per_person = int(input())  # cost_per_person - cost per person per night
        available_beds = list(map(int, input().split()))  # available_beds - available beds per night

        if min(available_beds) >= N:
            min_cost = min(min_cost, cost_per_person * N)

    print(min_cost if min_cost != B else "stay home")

if __name__ == "__main__":
    main()
