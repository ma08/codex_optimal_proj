
from collections import Counter

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    counts = Counter(arr)
    print(counts)
    print(max(counts))

    # if counts[max_roll] == 1:
    #     print(rolls.index(max_roll) + 1)
    # else:
    #     print("none")

if __name__ == "__main__":
    main()
