A, B, C, D = map(int, input().split())


P, M, G = map(int, input().split()) 


def get_dog_status(A, B, C, D, t): 
    t = (t - 1) % (A + B + C + D)
    if t < A: 
        return "A"
    elif t < A + B: 
        return "B"
    elif t < A + B + C: 
        return "C"
    else: 
        return "D"

    if get_dog_status(A, B, C, D, t) == "A" or get_dog_status(A, B, C, D, t) == "C": 
        return "aggressive"
    else: 
        return "calm"


def get_num_dogs_attacking(A, B, C, D, P): 
    dog1 = get_dog_status_at_time(A, B, C, D, P) 
    dog2 = get_dog_status_at_time(A, B, C, D, P) 
    if dog1 == "aggressive" and dog2 == "aggressive": 
        return "both"
    elif dog1 == "aggressive" or dog2 == "aggressive": 
        return "one"
    else: 
        return "none"


print(get_num_dogs_attacking(A, B, C, D, P)) 
print(get_num_dogs_attacking(A, B, C, D, M)) 
print(get_num_dogs_attacking(A, B, C, D, G)) 
