

def solution(N, A):
    counters = [0] * N

    #initialize the maximum counter
    max_counter = 0

    for i in A:
        if i <= N:
            #increase the counter at position i by 1
            counters[i - 1] += 1

            #update the maximum counter
            if counters[i - 1] > max_counter:
                max_counter = counters[i - 1]
        else:
            #set all counters to the maximum counter
            counters = [max_counter] * N

    return counters
