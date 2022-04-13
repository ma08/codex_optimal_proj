
A, B, C, D = map(int, input().split())
P, M, G = map(int, input().split())

def get_dog_status(A, B, C, D, t, dog):
    if dog == "A":
        t = (t - 1) % (A + B + C + D)
        if t < A:
            return "A"
        elif t < A + B:
            return "B"
        elif t < A + B + C:
            return "C"
        else:
            return "D"
    elif dog == "B":
        t = (t - 1) % (A + B + C + D)
        if t < A:
            return "B"
        elif t < A + B:
            return "C"
        elif t < A + B + C:
            return "D"
        else:
            return "A"
    elif dog == "C":
        t = (t - 1) % (A + B + C + D)
        if t < A:
            return "C"
        elif t < A + B:
            return "D"
        elif t < A + B + C:
            return "A"
        else:
            return "B"
    elif dog == "D":
        t = (t - 1) % (A + B + C + D)
        if t < A:
            return "D"
        elif t < A + B:
            return "A"
        elif t < A + B + C:
            return "B"
        else:
            return "C"

def get_dog_status_at_time(A, B, C, D, t, dog):
    if get_dog_status(A, B, C, D, t, dog) == "A" or get_dog_status(A, B, C, D, t, dog) == "C":
        return "aggressive"
    else:
        return "calm"

def get_num_dogs_attacking(A, B, C, D, P):
    dog1 = get_dog_status_at_time(A, B, C, D, P, "A")
    dog2 = get_dog_status_at_time(A, B, C, D, P, "B")
    if dog1 == "aggressive" and dog2 == "aggressive":
        return "both"
    elif dog1 == "aggressive" or dog2 == "aggressive":
        return "one"
    else:
        return "none"

print(get_num_dogs_attacking(A, B, C, D, P), get_num_dogs_attacking(A, B, C, D, M), get_num_dogs_attacking(A, B, C, D, G))
