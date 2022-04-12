

def main():
    """
    Main function
    """
    num_costumes = int(input())  # number of costumes
    costumes = []  # list of costumes
    for _ in range(num_costumes):  # loop through costumes
        costumes.append(input())  # add costume to list
    costume_set = set(costumes)  # set of costumes
    costume_counts = [costumes.count(costume) for costume in costume_set]  # count of costumes
    max_count = max(costume_counts)  # max count of costumes
    winners = [costume for costume, count in zip(costume_set, costume_counts) if count == max_count]  # winners
    print('\n'.join(sorted(winners)))

if __name__ == '__main__':
    main()
