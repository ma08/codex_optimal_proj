

#This is very simple.
#Since all values are integers, we know that the nearest integer to X is either X-1 or X+1.
#Thus, we just need to check if X-1 or X+1 is in the given sequence.
#If neither are in it, then we know the answer is X+1.
#If only one of them is in the sequence, then that one is the answer.
#If both are in the sequence, then the answer is X-1.

x = int(input().split()[0])
p = [int(i) for i in input().split()]

if x-1 not in p and x+1 not in p:
    print(x+1)
elif x-1 not in p:
    print(x-1)
elif x+1 not in p:
    print(x+1)
else:
    print(x-1)