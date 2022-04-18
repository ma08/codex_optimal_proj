

def main():
    """
    Main function
    """
    num_costumes = int(input())
    costumes = []
    for _ in range(num_costumes):
        costumes.append(input())
    costume_set = set(costumes) # set of unique costumes
    costume_counts = [costumes.count(costume) for costume in costume_set] # list of counts for each unique costume
    max_count = max(costume_counts) # get the maximum count
    winners = [costume for costume, count in zip(costume_set, costume_counts) if count == max_count] # list of winners
    print('\n'.join(sorted(winners))) # print winners in alphabetical order

if __name__ == "__main__":
    main()
