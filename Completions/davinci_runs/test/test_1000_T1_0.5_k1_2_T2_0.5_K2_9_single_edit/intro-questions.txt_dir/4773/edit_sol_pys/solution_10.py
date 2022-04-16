

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
    num_macro = 1
    
    # Loop through possible macro lengths
    while num_macro < num_chars:
        
        # The number of times the macro appears in the route
        num_times = 0
        
        # The length of the macro
        macro = route[:num_macro]
        
        # Loop through the route
        for i in range(num_chars - num_macro + 1):
            
            # If the route at the current index is equal to the macro, the macro is used
            if route[i:i+num_macro] == macro:
                num_times += 1
                
        # If the number of times the macro appears is greater than 1, the minimum number of characters needed is updated
        if num_times > 1:
            min_chars = min(min_chars, num_times + num_macro)
            
        # The length of the macro is increased
        num_macro += 1
        
    return min_chars

#-----Test Cases-----

print(min_chars('WNEENWEENEENE'))
print(min_chars('NSEW'))
