
number = int(input())
sequence = [number]

while True:
    if sequence[-1]%2 == 0:
        sequence.append(int(sequence[-1]/2))
    else:
        sequence.append(int(3*sequence[-1]+1))
    if sequence.count(sequence[-1]) == 2:
        print(sequence.index(sequence[-1])+1)
        break
