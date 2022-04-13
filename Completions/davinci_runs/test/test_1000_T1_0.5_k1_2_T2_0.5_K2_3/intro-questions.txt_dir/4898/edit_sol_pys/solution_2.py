

from itertools import combinations

def minion_preferences(s):
    n = int(s.readline())
    preferences = [sorted(map(int, s.readline().split())) for _ in range(n)]
    preferences.sort()
    return len(min(combinations(preferences, r) for r in range(len(preferences) + 1), key=lambda c: max(b - a for a, b in zip(c, c[1:]))))

if __name__ == "__main__":
    import sys
    print(minion_preferences(sys.stdin))
