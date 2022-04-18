def min_steps(n): 
    if n == 1: 
        return 0
    elif n == 2: 
        return 2
    elif n == 3: 
        return 3
    else: 
        return n - 1
  
n = 4
print(min_steps(n)) 
