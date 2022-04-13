

def main():
    gunnar_die_one = list(map(int, input().split()))
    gunnar_die_two = list(map(int, input().split()))
    emma_die_one = list(map(int, input().split()))
    emma_die_two = list(map(int, input().split()))

    gunnar_probability = calculate_probability(gunnar_die_one, gunnar_die_two)
    emma_probability = calculate_probability(emma_die_one, emma_die_two)

    if gunnar_probability > emma_probability:
        print("Gunnar")
    elif gunnar_probability < emma_probability:
        print("Emma")
    else:
        print("Tie")

def calculate_probability(die_one, die_two):
    sum_probability = 0
    for die_one_value in range(die_one[0], die_one[1]+1):
        for die_two_value in range(die_two[0], die_two[1]+1):
            sum_probability += 1/(die_one[1]-die_one[0]+1)/(die_two[1]-die_two[0]+1)
    return sum_probability

if __name__ == "__main__":
    main()
