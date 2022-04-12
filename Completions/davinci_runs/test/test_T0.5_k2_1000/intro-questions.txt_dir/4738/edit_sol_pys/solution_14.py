

def k_periodic_string(string):
    period = 1
    while period < len(string):
        if string[:-period] == string[period:]:
            return period
        period += 1
    return len(string)

print(k_periodic_string(input()))
