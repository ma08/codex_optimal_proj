
#-----Solution-----

def min_chars(route):
    """
    Returns the minimum number of characters needed to transmit a route to a rover
    """
    # The minimum number of characters needed to transmit the route
    min_chars = len(route)
    
    # The number of characters in the route
    num_chars = len(route)
    
    # The number of characters in the marker
    num_marker = 1
    
    while num_marker < num_chars:
        
        # The number of times the marker appears in the route
        num_times = 0
        
        # The length of the marker
        marker = route[:num_marker]
        
        # Loop through the route
        for i in range(num_chars - num_marker + 1):
            
            # If the route at the current index is equal to the marker, the marker is used
            if route[i:i+num_marker] == marker:
                num_times += 1
                
        # If the number of times the marker appears is greater than 1, the minimum number of characters needed is updated
        if num_times > 1:
            min_chars = min(min_chars, num_times + num_marker)
            
        # The length of the marker is increased
        num_marker += 1
        
    return min_chars

#-----Test Cases-----
print(min_chars('WNEENWEENEENE'))
print(min_chars('NSEW'))
