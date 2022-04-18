

def main():
    """
    Main function
    """
    num_costumes = int(input())
    costumes = []
    for _ in range(num_costumes):
        costumes.append(input())
    costume_set = set(costumes)
    costume_counts = [costumes.count(costume) for costume in costume_set]    
    winners = sorted([costume for costume, count in zip(costume_set, costume_counts) if count == max(costume_counts)])
    print('\n'.join(winners))

if __name__ == "__main__":
    main()
