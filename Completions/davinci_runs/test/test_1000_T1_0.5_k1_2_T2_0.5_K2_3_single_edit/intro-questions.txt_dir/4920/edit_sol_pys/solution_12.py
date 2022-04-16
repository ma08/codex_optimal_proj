

# I/O
input_string = raw_input()

# Solution
def count_itineraries(input_string):
    """
    Returns the number of itineraries for a given input string.
    An itinerary is a sequence of at least two events in the summer
    season where the first and last events are of different types,
    and they are both unique among all event types during the sequence.
    """
    # Initialize dictionary to store event types
    event_types = {}
    # Initialize variable to store number of itineraries
    itineraries = 0
    # Iterate through the input string
    for event in input_string:
        # Check if event type is in the dictionary
        if event in event_types:
            # Increment value of event type by 1
            event_types[event] += 1
        else:
            # Add event type to dictionary with value of 1
            event_types[event] = 1
        # Check if there are at least two different event types
        if len(event_types) >= 2:
            # Iterate through event types in dictionary
            for event_type in event_types:
                # Check if event type is the first one in the input string
                if event_type == input_string[0]:
                    # Increment number of itineraries by the number of
                    # events of the current type
                    itineraries += event_types[event_type]
                else:
                    # Increment number of itineraries by 1
                    itineraries += 1
    # Return number of itineraries
    return itineraries

# Output
print(count_itineraries(input_string))
