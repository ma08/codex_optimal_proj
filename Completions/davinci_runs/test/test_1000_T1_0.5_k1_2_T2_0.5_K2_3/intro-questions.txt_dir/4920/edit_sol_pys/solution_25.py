

import sys

def main():
    events = sys.stdin.readlines()
    num_events = len(events[0])

    # Build a list of the number of occurrences of each event type
    counts = [0 for i in xrange(26)]
    for c in events[0]:
        counts[ord(c) - ord('a')] += 1

    # Compute the number of good itineraries
    num_good = 0
    for i in xrange(26):
        num_good += counts[i] * (num_events - counts[i])

    print (num_good)

if __name__ == "__main__":
    main()
