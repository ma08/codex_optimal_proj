

def main():
    """
    Main function
    """
    num_costumes = int(input())
    costumes = []
    for _ in range(num_costumes):
        costumes.append(input())
    print('\n'.join(sorted(set(costumes))))

if __name__ == "__main__":
    main()
