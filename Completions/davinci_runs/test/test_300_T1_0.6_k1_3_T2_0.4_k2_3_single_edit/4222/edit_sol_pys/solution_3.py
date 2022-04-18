

def main():
    """
    1. read input and get number of snukes and snacks
    2. store input in a list
    3. loop through the list and if the number of a snukes is not in the list, then add it to the victim list
    4. print out the length of the victim list
    """
    snuke_and_snack_count = [int(i) for i in input().split()]  # 1.
    snuke_count = snuke_and_snack_count[0]
    snack_count = snuke_and_snack_count[1]
    input_list = []
    victim_list = []
    for i in range(snack_count):
        input_list += [int(i) for i in input().split()]  # 2.
    for i in range(1, snuke_count + 1):
        if i not in input_list:
            victim_list.append(i)
    print(len(victim_list))
if __name__ == '__main__':
    main()
