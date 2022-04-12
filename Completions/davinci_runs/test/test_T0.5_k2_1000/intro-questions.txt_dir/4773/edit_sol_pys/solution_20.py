
#-----Solution-----

def min_chars(route):
    """
    Returns the minimum number of characters needed to transmit a route to a rover
    """
    # The minimum number of characters needed to transmit the route is the length of the route
    min_chars = len(route)
    
    # The number of characters in the pattern
    num_pattern = 0

    while num_pattern < len(route):
        
        # The length of the pattern
        pattern = route[:num_pattern]

        # The number of times the pattern appears in the route
        num_times = route.count(pattern)

        # If the number of times the pattern appears is greater than 1, the minimum number of characters needed is updated
        if num_times > 1:
            min_chars = min(min_chars, num_times + num_pattern)
            
        # The length of the pattern is increased by 1
        num_pattern += 1

    return min_chars

#-----Test Cases-----

print(min_chars('WNEENWEENEENE'))
print(min_chars('NSEW'))
