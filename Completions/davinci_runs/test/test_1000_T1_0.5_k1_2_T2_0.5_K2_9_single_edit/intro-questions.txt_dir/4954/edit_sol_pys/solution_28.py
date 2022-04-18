

def main():
    n, b, h, w = map(int, input().split())
    min_cost = b

    for _ in range(h):
        cost_per_person = int(input())
        available_beds = list(map(int, input().split()))

        for beds in available_beds:
            if beds >= n:
                min_cost = min(min_cost, cost_per_person * n)

    if min_cost == b:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
