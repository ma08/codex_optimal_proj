

def main():
    gunnar_dice_one = list(map(int, input().split(" ")))
    gunnar_dice_two = list(map(int, input().split(" ")))
    emma_dice_one = list(map(int, input().split(" ")))
    emma_dice_two = list(map(int, input().split(" ")))

    gunnar_probability = calculate_probability(gunnar_dice_one, gunnar_dice_two)
    emma_probability = calculate_probability(emma_dice_one, emma_dice_two)

    if gunnar_probability > emma_probability:
        print("Gunnar")
    elif gunnar_probability < emma_probability:
        print("Emma")
    else:
        print("Tie")

def calculate_probability(dice_one, dice_two):
    sum_probability = 0
    for die_one in range(dice_one[0], dice_one[1]+1):
        for die_two in range(dice_two[0], dice_two[1]+1):
            sum_probability += 1/(dice_one[1]-dice_one[0]+1)/(dice_two[1]-dice_two[0]+1)
    return sum_probability

if __name__ == "__main__":
    main()
