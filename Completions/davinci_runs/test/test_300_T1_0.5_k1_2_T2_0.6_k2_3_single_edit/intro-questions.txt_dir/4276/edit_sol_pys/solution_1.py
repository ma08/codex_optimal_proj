
N, T = map(int, input().split())  # N:num of program, T:max time
costs = []                         # list of cost
times = []                         # list of time
for i in range(N):                 # input
    c, t = map(int, input().split())  # cost, time
    costs.append(c)                 
    times.append(t)
costs = [costs[i] for i in range(len(costs)) if times[i] <= T]  # get programs which can be done in T
if len(costs) == 0:                                             # if there are no programs, print TLE
    print('TLE')                   
else:                               # if there is at least one program, print min of cost
    print(min(costs))              
