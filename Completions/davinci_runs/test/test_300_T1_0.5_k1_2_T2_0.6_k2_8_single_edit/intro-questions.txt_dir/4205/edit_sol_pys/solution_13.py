
N = int(input())
sequence = list(map(int, input().split())) #get sequence
if(sequence == sorted(sequence)): # if sequence is sorted
    print("YES") #print yes
else: #if sequence is not sorted
    print("NO") #print no
