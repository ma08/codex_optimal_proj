

S, C, K = map(int, input().split())
socks = list(map(int, input().split()))
# print(socks)
socks.sort()

machines = 0

while len(socks) > 0:
    current_machine = []
    current_machine.append(socks.pop(0))
    while len(current_machine) < C and len(socks) > 0:
        if abs(current_machine[-1] - socks[0]) <= K:
            current_machine.append(socks.pop(0))
        else:
            break
    machines += 1

print(machines)