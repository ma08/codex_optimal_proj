from collections import defaultdict


def get_mode(numbers):
    counts = defaultdict(int)
    for n in numbers:
        counts[n] += 1
    max_count = max(counts.values())
    modes = [n for n, count in counts.items() if count == max_count]
    return modes
