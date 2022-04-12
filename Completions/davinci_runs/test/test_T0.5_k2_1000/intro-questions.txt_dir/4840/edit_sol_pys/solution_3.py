

def main():
    gunnar_die_one = list(map(int, input().split()))
    gunnar_die_two = list(map(int, input().split()))
    emma_die_one = list(map(int, input().split()))
    emma_die_two = list(map(int, input().split()))

    gunnar_probability = calculate_probability(gunnar_die_one[0], gunnar_die_one[1], gunnar_die_two[0], gunnar_die_two[1])
    emma_probability = calculate_probability(emma_die_one[0], emma_die_one[1], emma_die_two[0], emma_die_two[1])

    if gunnar_probability > emma_probability:
        print("Gunnar")
    elif gunnar_probability < emma_probability:
        print("Emma")
    else:
        print("Tie")

def calculate_probability(die_one_min, die_one_max, die_two_min, die_two_max):
    sum_probability = 0
    for die_one in range(die_one_min, die_one_max+1):
        for die_two in range(die_two_min, die_two_max+1):
            sum_probability += 1/(die_one_max-die_one_min+1)/(die_two_max-die_two_min+1)
    return sum_probability

if __name__ == "__main__":
    main()
