

S, C, K = map(int, input().split()) # S: socks, C: capacity, K: tolerance
socks = list(map(int, input().split()))

socks.sort()

machines = 0 # number of machines

while len(socks) > 0:

    # append first sock
    current_machine = []

    # append socks that are within tolerance range
    current_machine.append(socks.pop(0))
    while len(current_machine) < C and len(socks) > 0:
        if abs(current_machine[-1] - socks[0]) <= K:
            current_machine.append(socks.pop(0))
        else:

    # machine is full, move to next machine
            break
    machines += 1

print(machines)
