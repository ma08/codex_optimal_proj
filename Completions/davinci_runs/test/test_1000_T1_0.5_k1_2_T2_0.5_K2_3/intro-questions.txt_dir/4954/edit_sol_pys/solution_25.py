

def main():
    num_people, budget, num_hotels, num_weeks = [int(x) for x in input().split()]
    min_cost = budget + 1
    for _ in range(num_hotels):
        cost_per_person = int(input())
        for beds in [int(x) for x in input().split()]:
            if beds >= num_people:
                min_cost = min(min_cost, num_people * cost_per_person)
    if min_cost <= budget:
        print(min_cost)
    else:
        print("stay home")

if __name__ == '__main__':
    main()
