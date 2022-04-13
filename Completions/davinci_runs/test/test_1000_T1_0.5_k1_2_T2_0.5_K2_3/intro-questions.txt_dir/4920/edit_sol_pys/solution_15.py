
# I/O
input_string = input()

def count_itineraries(input_string):
    # Solution
    """
    Returns the number of itineraries for a given input string.
    An itinerary is a sequence of at least two events in the winter
    season where the first and last events are of different types,
    and they are both unique among all event types during the sequence.
    """
    # Initialize dictionary to store event types and counts
    event_types = {}
    # Initialize variable to store number of itineraries as 0
    itineraries = 1
    # Iterate through the input string, starting from the second event
    for i in range(1, len(input_string)):
        # Check if the current event type is in the dictionary
        if input_string[i] in event_types:
            # Increment the value of the current event type by 1
            event_types[input_string[i]] += 1
        else:
            # Add the current event type to the dictionary with value of 1
            event_types[input_string[i]] = 1
        # Check if there are at least two different event types in the
        # dictionary
        if len(event_types) > 1:
            # Iterate through event types in the dictionary
            for key in event_types:
                # Check if the current event type is the first one in the
                # input string
                if key == input_string[0]:
                    # Increment the number of itineraries by the number of
                    # events of the current type and the number of events of
                    # the first type
                    itineraries += event_types[key] * event_types[input_string[0]]
                # Check if the current event type is not the first one in the
                # input string
                elif key != input_string[0]:
                    # Increment the number of itineraries by the number of
                    # events of the current type and the number of events of
                    # the first type
                    itineraries += event_types[key] * event_types[input_string[0]]
    # Return the number of itineraries
    return itineraries

# Output
print(count_itineraries(input_string))
