

def check_proof(proof):
    assumptions = []
    for line in proof:
        line = line.split('->')
        if line[0].strip() == '':
            assumptions.append(line[1].strip())
        else:
            for assumption in line[0].split():
                if assumption not in assumptions:
                    return proof.index(line) + 1, '|-', line[1].strip()
            assumptions.append(line[1].strip())
    return 'correct'

if __name__ == '__main__':
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())
    print(check_proof(proof))
