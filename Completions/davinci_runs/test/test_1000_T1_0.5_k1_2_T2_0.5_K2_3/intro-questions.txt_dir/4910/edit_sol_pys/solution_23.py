

def main():
    """
    Main function
    """
    num_costume = int(input())
    costume = []
    for _ in range(num_costume):
        costume.append(input())
    costume_set = set(costume)
    costume_count = [costume.count(costume) for costume in costume_set]
    max_count = max(costume_count)
    winners = [costume for costume, count in zip(costume_set, costume_count) if count == max_count]
    print('\n'.join(sorted(winners)))

if __name__ == "__main__":
    main()
