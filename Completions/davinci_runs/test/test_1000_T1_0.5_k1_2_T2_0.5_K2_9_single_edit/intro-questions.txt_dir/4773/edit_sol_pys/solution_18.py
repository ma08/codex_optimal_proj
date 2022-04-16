

#-----Solution-----

def min_chars(route):
    """
    Returns the minimum number of characters needed to transmit a route to a rover
    """
    # The minimum number of characters needed to transmit the route
    min_chars = len(route)
    
    # The number of characters in the route
    num_chars = len(route)
    
    # The number of characters in the macro
    macro_len = 1
    
    # Loop through possible macro lengths
    while macro_len < num_chars:
        
        # The number of times the macro appears in the route
        num_times = 0
        
        # The length of the macro
        macro = route[:macro_len]
        
        # Loop through the route
        for i in range(num_chars - macro_len + 1):
            
            # If the route at the current index is equal to the macro, the macro is used
            if route[i:i+macro_len] == macro:
                num_times += 1
                
        # If the number of times the macro appears is greater than 1, the minimum number of characters needed is updated
        if num_times > 1:
            min_chars = min(min_chars, num_times + macro_len)
            
        # The length of the macro is increased
        macro_len += 1
        
    return min_chars

#-----Test Cases-----

print(min_chars('WNEENWEENEENE'))
print(min_chars('NSEW'))
