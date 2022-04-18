
# I/O
input_string = input()

# Solution
def count_itineraries(input_string):
    """
    Returns the number of itineraries for a given input string.
    An itinerary is a sequence of at least two events in the summer
    season where the first and last events are of different types,
    and they are both unique among all event types during the sequence.
    """
    # Initialize dictionary to store event types and occurrences
    event_types = {}
    itineraries = 0
    for i in range(len(input_string)):
        # Check if event type is in the dictionary and increment accordingly
        if input_string[i] in event_types:
            event_types[input_string[i]] += 1
        else:
            event_types[input_string[i]] = 1
        # Check if there are at least two different event types
        if len(event_types) >= 2:
            # Iterate through event types in dictionary and increment accordingly
            for event_type in event_types:
                if event_type == input_string[0]:
                    itineraries += event_types[event_type]
                else:
                    itineraries += 1
    # Return number of itineraries
    return itineraries

# Output
print(count_itineraries(input_string))
