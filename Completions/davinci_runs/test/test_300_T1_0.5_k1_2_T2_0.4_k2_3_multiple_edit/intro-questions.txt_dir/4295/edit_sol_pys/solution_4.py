
N, K = map(int, input().split()) # N and K is input

if N % K == 0: # if N is divisible by K
    print(0) # print 0
else:
    print(min(N % K, K - (N % K)))
