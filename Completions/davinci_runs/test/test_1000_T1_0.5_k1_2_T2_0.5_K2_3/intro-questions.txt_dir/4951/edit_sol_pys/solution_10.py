

def check_proofs(proof):
    assumptions = set()
    for i, line in enumerate(proof):
        line = line.split(' -> ')
        if line[0] == '':
            assumptions.add(line[1])
        else:
            line[0] = line[0].split()
            for j in range(len(line[0])):
                if line[0][j] not in assumptions:
                    return i + 1
            assumptions.add(line[1])
    return 'correct'

if __name__ == '__main__':
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())
    print(check_proofs(proof))
