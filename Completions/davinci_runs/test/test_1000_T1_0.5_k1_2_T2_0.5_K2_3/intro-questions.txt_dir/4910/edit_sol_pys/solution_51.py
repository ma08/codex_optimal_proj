

import sys

def main():
    """
    Main function
    """
    num_costumes = int(input())
    costumes = []
    for _ in range(num_costumes):
        costumes.append(input())
    costumes_set = set(costumes)
    costumes_counts = [costumes.count(costume) for costume in sorted(costumes_set)]
    max_count = max(costumes_counts)
    winners = [costume for costume, count in zip(sorted(costumes_set), costumes_counts) if count == max_count]
    print('\n'.join(sorted(winners)))

if __name__ == "__main__":
    sys.exit(main())
