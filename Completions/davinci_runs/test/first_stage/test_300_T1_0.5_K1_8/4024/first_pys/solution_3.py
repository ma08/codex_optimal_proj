

def main():
    # parse input
    n, k = map(int, input().split())
    s = input()

    # build subsequence generator
    def subsequences(s):
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                yield s[i:j]

    # determine if it is possible to generate the set
    def possible(s, k):
        # build set of all subsequences of s
        subsequences_set = set(subsequences(s))
        # build list of costs to generate each subsequence
        costs = [len(s) - len(subsequence) for subsequence in subsequences_set]
        # sort costs
        costs.sort()
        # return sum of first k costs
        return sum(costs[:k])

    # print result
    print(possible(s, k) if possible(s, k) != 0 else -1)

if __name__ == "__main__":
    main()