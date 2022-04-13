
s = input()

def get_min_distance(s):
    min_distance = 10000
    for i in range(len(s) - 2):
        x = int(s[i:i+3])
        diff = abs(x - 753)
        if diff < min_distance:
            min_distance = diff
    return min_distance

print(get_min_distance(s))
