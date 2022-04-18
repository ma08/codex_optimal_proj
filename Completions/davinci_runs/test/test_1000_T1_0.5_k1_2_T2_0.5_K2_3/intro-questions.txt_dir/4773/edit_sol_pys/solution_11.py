

#-----Solution-----

def min_chars(route_in):
    """
    Returns the minimum number of characters needed to transmit a route to a rover
    """
    # The minimum number of characters needed to transmit the route
    min_chars_out = len(route_in)
    
    # The number of characters in the route
    num_chars = len(route_in)
    
    # The number of characters in the pattern
    num_pattern = 1
    
    while num_pattern < num_chars:
        
        # The number of times the pattern appears in the route
        num_times = 0
        
        # The length of the pattern
        pattern = route_in[:num_pattern]
        
        # Loop through the route
        for i in range(num_chars - num_pattern + 1):
            
            # If the route at the current index is equal to the pattern, the pattern is used
            if route_in[i:i+num_pattern] == pattern:
                num_times += 1
                
        # If the number of times the pattern appears is greater than 1, the minimum number of characters needed is updated
        if num_times > 1:
            min_chars_out = min(min_chars_out, num_times + num_pattern)
            
        # The length of the pattern is increased
        num_pattern += 1
        
    return min_chars_out

#-----Test Cases-----

print(min_chars('WNEENWEENEENE'))
print(min_chars('NSEW'))
