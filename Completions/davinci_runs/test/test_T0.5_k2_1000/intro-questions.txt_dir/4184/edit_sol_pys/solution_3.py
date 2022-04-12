N = int(input()) 
A = list(map(int, input().split())) 
 
count = 0 
while True: 
    for i in range(N): 
        if A[i] % 2 != 0: 
            print(count) 
            exit() 
        A[i] /= 2 
    count += 1
