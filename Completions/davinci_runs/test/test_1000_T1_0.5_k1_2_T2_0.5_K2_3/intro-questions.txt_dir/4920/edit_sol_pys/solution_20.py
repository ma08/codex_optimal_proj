

import sys

def main():
    events = sys.stdin.readlines()[0].strip() #read the input file
    num_events = len(events) #count the number of events

    # Build a list of the number of occurrences of each event type 
    counts = [0 for i in xrange(26)] #create a list of 26 zeros
    for c in events: #for each character in the file
        counts[ord(c) - ord('a')] += 1 #increment the count for each character

    # Compute the number of good itineraries 
    num_good = 0
    for i in xrange(26): #for each character in the alphabet
        num_good += counts[i] * (num_events - counts[i]) #num_good = sum of counts * (num_events - counts)

    print num_good #print the number of good itineraries

if __name__ == "__main__":
    main()
