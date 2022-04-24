

N = int(input())
sequence = list(map(int, input().split()))
# a = [1,2,3,4,5]
# b = [5,4,3,2,1]
if(sequence == sorted(sequence)):
    exit()
    print("YES")
for i in range(N):
    if sequence[i] > sequence[i + 1]:
        print(i)
        break
else:
for j in range(N - 1, -1, -1):
    if sequence[j] < sequence[j - 1]:
        print(j)
        break


    print("NO")
